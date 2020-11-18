from django.db import models
from simple_history.models import HistoricalRecords
from django.utils import timezone
from django.utils.timezone import localtime


class CommonCategory(models.Model):
    name = models.CharField('Name', max_length=80, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class SnMixin(models.Model):
    SN_LENGTH = 3
    sn_prefix = 'SN'
    sn = models.CharField(max_length=32, editable=False, blank=True, unique=True)

    class Meta:
        abstract = True

    def _generate_sn(self) -> str:
        if self.sn:
            return self.sn

        model = self._meta.model
        if hasattr(self, 'date'):
            new_sn_date_str = str(self.date)
            latest_obj = model.objects.with_deleted().filter(date=self.date).exclude(sn='').order_by('id').last()
        elif hasattr(self, 'created_at'):
            new_sn_date_str = str(
                self.created_at and localtime(self.created_at).date() or localtime(timezone.now()).date()
            )
            latest_obj = model.objects.with_deleted().filter(created_at__date=new_sn_date_str).exclude(sn='').order_by(
                'id').last()
        else:
            return ''

        if latest_obj and latest_obj.sn:
            sn_id = latest_obj.sn[-self.SN_LENGTH:]
            assert sn_id.isnumeric(), "SN last {} characters cannot combines a number".format(self.SN_LENGTH)
            new_sn_id = int(sn_id) + 1
        else:
            new_sn_id = 1

        new_sn_id_str = str(new_sn_id)
        new_sn_date_str = new_sn_date_str.replace('-', '')[2:]
        new_sn = '{}{}{}'.format(self.sn_prefix, new_sn_date_str, new_sn_id_str.zfill(self.SN_LENGTH))
        return new_sn

    def save(self, *args, **kwargs):
        if not self.sn:
            self.sn = self._generate_sn()
        super().save(*args, **kwargs)
