from django.db import models
from .base_managers import CommonManager
from .enums import STATUS_DELETED, MSG_NOT_FOUND


class BaseModel(models.Model):
    """Abstract DB Base Model"""
    CreatedByID = models.CharField(db_column='CreatedByID', max_length=50, blank=True, null=True, editable=False)
    CreatedAt = models.DateTimeField(db_column='CreatedAt', auto_now_add=True, editable=False)
    UpdatedByID = models.CharField(db_column='UpdatedByID', max_length=50, blank=True, null=True, editable=False)
    UpdatedAt = models.DateTimeField(db_column='UpdatedAt', auto_now=True, editable=False)
    Status = models.SmallIntegerField(db_column='Status', default=1)
    Cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)
    objects = CommonManager()

    class Meta:
        abstract = True
        ordering = ('-id',)

    def delete(self):
        self.Status = STATUS_DELETED
        super().save()

    def created_by(self):
        from .models import UserInfo
        created_by = None
        if self.CreatedByID:
            created_by = UserInfo.objects.with_deleted().filter(UserID=self.CreatedByID).first()
        return created_by and created_by.username() or MSG_NOT_FOUND

    def _do_insert(self, manager, using, fields, returning_fields, raw):
        fields = [f for f in fields if f.attname not in ['SN', 'Cdate']]
        ret = super()._do_insert(manager, using, fields, returning_fields, raw)
        return ret

    def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
        values = [f for f in values if f[0].attname not in ['SN', 'Cdate']]
        ret = super()._do_update(base_qs, using, pk_val, values, update_fields, forced_update)
        return ret
