from django.db import models
from .base_managers import CommonManager
from .enums import STATUS_DELETED, MSG_NOT_FOUND


class BaseModel(models.Model):
    """Abstract DB Base Model"""
    CreatedByID = models.CharField(db_column='CreatedByID', max_length=50, blank=True, null=True, editable=False)
    CreatedAt = models.DateTimeField(db_column='CreatedAt', auto_now_add=True, editable=False)
    UpdatedByID = models.CharField(db_column='UpdatedByID', max_length=50, blank=True, null=True, editable=False)
    UpdatedAt = models.DateTimeField(db_column='UpdatedAt', auto_now=True, editable=False)
    Status = models.SmallIntegerField(db_column='Status', blank=True, null=True)
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
            created_by = UserInfo.objects.get_or_none(UserID=self.CreatedByID)
        return created_by and created_by.username() or MSG_NOT_FOUND
