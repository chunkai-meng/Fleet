from django.db import models
from .base_managers import CommonManager
from .enums import STATUS_DELETED


class BaseModel(models.Model):
    """Abstract DB Base Model"""
    CreatedByID = models.CharField(db_column='CreatedByID', max_length=32, blank=True, null=True)
    CreatedAt = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    UpdatedByID = models.CharField(db_column='UpdatedByID', max_length=32, blank=True, null=True)
    UpdatedAt = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    OriginalID = models.IntegerField(db_column='OriginalID', blank=True, null=True)
    Status = models.SmallIntegerField(db_column='Status', blank=True, null=True)
    Cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)
    objects = CommonManager()

    class Meta:
        abstract = True
        ordering = ('-id',)

    def delete(self):
        self.Status = STATUS_DELETED
        super().save()
