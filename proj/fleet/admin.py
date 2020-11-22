from django.contrib import admin
from .models import UserInfo


# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    # list_display = ('user_id', 'firstname', 'lastname', 'email_address', 'status', 'created_at')
    list_display = (
    'id', 'UserID', 'DepartmentID', 'DriverLicense', 'EmailAddress', 'LicenseClass', 'LicenseExpiryDate',
    'Mobile', 'Role', 'username'
    )
