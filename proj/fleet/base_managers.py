from django.db import models

STATUS_DELETED = -1


class CommonQuerySet(models.QuerySet):
    def delete(self):
        self.update(Status=STATUS_DELETED)


class CommonManager(models.Manager):
    use_for_related_fields = True

    def with_deleted(self):
        return CommonQuerySet(self.model, using=self._db)

    def deleted(self):
        return self.with_deleted().filter(Status=STATUS_DELETED)

    def get_queryset(self):
        return self.with_deleted().exclude(Status=STATUS_DELETED)
