from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords
from django.utils.crypto import get_random_string
import uuid


def get_non_ad_sid():
    return 'NON-AD-USER-' + get_random_string()


class UserInfo(models.Model):
    user_id = models.CharField(db_column='UserID', max_length=50)
    firstname = models.CharField(db_column='FirstName', max_length=50)
    lastname = models.CharField(db_column='LastName', max_length=50)
    driver_license = models.CharField(db_column='DriverLicense', max_length=50, blank=True, null=True)
    email_address = models.CharField(db_column='EmailAddress', max_length=50, blank=True, null=True)
    department_id = models.CharField(db_column='DepartmentID', max_length=50, blank=True, null=True)
    license_class = models.CharField(db_column='LicenseClass', max_length=30, blank=True, null=True)
    license_expiry_date = models.DateTimeField(db_column='LicenseExpiryDate', blank=True, null=True)
    role = models.SmallIntegerField(db_column='Role', blank=True, null=True)
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)
    created_by_id = models.CharField(db_column='CreatedByID', max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_by_id = models.CharField(db_column='UpdatedByID', max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    original_id = models.IntegerField(db_column='OriginalID', blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserInfo'


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
    object_sid = models.CharField(max_length=256, default=get_non_ad_sid, unique=True)
    sam_account_name = models.CharField(max_length=256, default=get_random_string, unique=True)
    history = HistoricalRecords(app="audit", custom_model_name=lambda x: f'Account{x}')

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.username
