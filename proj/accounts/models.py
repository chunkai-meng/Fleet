from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords
from django.utils.crypto import get_random_string
import uuid


def get_non_ad_sid():
    return 'NON-AD-USER-' + get_random_string()


# Create your models here.
class UserProfile(AbstractUser):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('D', 'Gender Diverse'),
    )
    # Rename to match Sandy's DB
    first_name = models.CharField(max_length=50, db_column='FirstName')
    last_name = models.CharField(max_length=50, db_column='LastName')
    phone_number = models.CharField("Mobile", max_length=50, blank=True, null=True, db_column='Mobile')
    # Added to match
    user_id = models.UUIDField(max_length=50, default=uuid.uuid4, editable=False, db_column='UserID')
    driver_license = models.CharField(max_length=50, blank=True, db_column='DriverLicense')
    email = models.CharField(max_length=50, blank=True, db_column='EmailAddress')
    department_id = models.CharField(max_length=50, blank=True, db_column='DepartmentID')
    license_class = models.CharField(max_length=50, blank=True, db_column='LicenseClass')
    license_expiry_date = models.DateTimeField(blank=True, null=True, db_column='LicenseExpiryDate')
    role = models.SmallIntegerField(blank=True, null=True, db_column='Role')
    status = models.IntegerField(blank=True, null=True, db_column='Status')
    created_by_id = models.CharField(max_length=32, blank=True, db_column='CreatedByID')
    created_at = models.DateTimeField(blank=True, null=True, db_column='CreatedAt')
    updated_by_id = models.CharField(max_length=32, blank=True, db_column='UpdatedByID')
    updated_at = models.DateTimeField(blank=True, null=True, db_column='UpdatedAt')
    original_id = models.IntegerField(blank=True, null=True, db_column='OriginalID')
    cdate = models.DateTimeField(blank=True, null=True, db_column='Cdate')

    cn_name = models.CharField(max_length=80, blank=True, null=True)
    display_name = models.CharField(max_length=80, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER, blank=True, null=True)

    ou_dc = models.CharField(max_length=256, blank=True)
    employee_id = models.CharField(max_length=256, blank=True)
    cost_center = models.CharField(max_length=256, blank=True)
    object_sid = models.CharField(max_length=256, blank=True)
    sam_account_name = models.CharField(max_length=256, blank=True)

    # history = HistoricalRecords(app="audit", custom_model_name=lambda x: f'Account{x}')

    class Meta:
        db_table = 'UserProfile'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.username
