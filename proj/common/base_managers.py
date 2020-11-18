from django.db import models
from utils.formats import validate_date


class CommonQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted=True)

    def date_during(self, start_date='', end_date=''):
        if validate_date(start_date) and validate_date(end_date):
            return self.filter(date__range=[start_date, end_date])
        elif validate_date(start_date):
            return self.filter(date__gte=start_date)
        elif validate_date(end_date):
            return self.filter(date__lte=end_date)
        else:
            return self


class CommonManager(models.Manager):
    use_for_related_fields = True

    # def get_queryset(self):
    #     return CommonQuerySet(self.model, using=self._db)  # Important!

    def with_deleted(self):
        return CommonQuerySet(self.model, using=self._db)

    def deleted(self):
        return self.with_deleted().filter(deleted=True)

    def get_queryset(self):
        return self.with_deleted().exclude(deleted=True)

    # def all_valid(self):
    #     return self.get_queryset().all_valid()
    #
    # def all_invalid(self):
    #     return self.get_queryset().all_invalid()
    #
    # def date_during(self, start_date='', end_date=''):
    #     return self.get_queryset().date_during(start_date, end_date)
