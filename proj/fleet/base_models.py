from django.db import models
from django.conf import settings
from .base_managers import CommonManager


class BaseModel(models.Model):
    """Abstract DB Base Model"""
    created_by_id = models.CharField(db_column='CreatedByID', max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_by_id = models.CharField(db_column='UpdatedByID', max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    original_id = models.IntegerField(db_column='OriginalID', blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)
    cdate = models.DateTimeField('CDate', db_column='Cdate', blank=True, null=True)
    objects = CommonManager()

    class Meta:
        abstract = True
        ordering = ('-id',)
