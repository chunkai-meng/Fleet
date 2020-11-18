from django.db import models
from django.conf import settings
from common.base_managers import CommonManager


class BaseModel(models.Model):
    """Abstract DB Base Model"""
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True,
        on_delete=models.SET_NULL,
        editable=False, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True,
        on_delete=models.SET_NULL,
        editable=False, related_name="+")
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    delete_reason = models.CharField(max_length=2048, blank=True)
    deleted = models.BooleanField(default=False)
    objects = CommonManager()

    class Meta:
        abstract = True
        ordering = ('-id',)

    def __str__(self):
        if hasattr(self, 'sn'):
            return self.sn
        else:
            return self.id

    def delete(self, delete_reason=''):
        self.deleted = True
        self.delete_reason = delete_reason
        self.save()

    # def hard_delete(self):
    #     super().delete()
