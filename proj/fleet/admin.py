from django.contrib import admin
from .models import UserInfo, ServiceForm, WorkshopInfo, Infringement


# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    # list_display = ('user_id', 'firstname', 'lastname', 'email_address', 'status', 'created_at')
    list_display = (
        'id', 'UserID', 'DepartmentID', 'DriverLicense', 'EmailAddress', 'LicenseClass', 'LicenseExpiryDate',
        'Mobile', 'Role', 'username'
    )


@admin.register(ServiceForm)
class ServiceFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'SN', 'StartDate', 'EndDate', 'PlateNumber', 'WorkshopID', 'ServiceName', 'ServicePrice')
    readonly_fields = ('SN', 'Status')


@admin.register(WorkshopInfo)
class WorkshopInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'WorkshopID', 'WorkshopName', 'Address', 'ContactPerson', 'ContactPhone', 'Email')
    readonly_fields = ('WorkshopID', 'Status')


@admin.register(Infringement)
class InfringementAdmin(admin.ModelAdmin):
    list_display = ('id', 'Amount', 'created_by', 'Date', 'InfringementNumber', 'PaidDate',
                    'PlateNumber', 'Status', 'UserID', 'user_name')
    readonly_fields = ('user_name', 'Status')
