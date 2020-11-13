from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords
from django.utils.crypto import get_random_string


def get_non_ad_sid():
    return 'NON-AD-USER-' + get_random_string()


# Create your models here.
class UserProfile(AbstractUser):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('D', 'Gender Diverse'),
    )
    cn_name = models.CharField(max_length=80, blank=True, null=True)
    display_name = models.CharField(max_length=80, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER, blank=True, null=True)
    phone_number = models.CharField("Phone Number",
                                    max_length=16, blank=True, null=True)
    ou_dc = models.CharField(max_length=256, blank=True)
    employee_id = models.CharField(max_length=256, blank=True)
    cost_center = models.CharField(max_length=256, blank=True)
    object_sid = models.CharField(max_length=256, blank=True)
    sam_account_name = models.CharField(max_length=256, blank=True)
    history = HistoricalRecords(app="audit", custom_model_name=lambda x: f'Account{x}')

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.username
