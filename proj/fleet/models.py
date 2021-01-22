# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid
from django.db import models, connection
from .base_models import BaseModel
from .base_managers import CommonManager
from . import enums


class UserInfo(BaseModel):
    SAMAccountName = models.CharField(db_column='SAMAccountName', max_length=50, unique=True)
    UserID = models.UUIDField(db_column='UserID', max_length=50, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(db_column='FirstName', max_length=50)
    LastName = models.CharField(db_column='LastName', max_length=50)
    DriverLicense = models.CharField(db_column='DriverLicense', max_length=50)
    EmailAddress = models.CharField(db_column='EmailAddress', max_length=50)
    DepartmentID = models.CharField(db_column='DepartmentID', max_length=50)
    LicenseClass = models.CharField(db_column='LicenseClass', max_length=30)
    LicenseExpiryDate = models.DateField(db_column='LicenseExpiryDate', null=True)
    Role = models.SmallIntegerField(db_column='Role', choices=enums.USERINFO_ROLE_CHOICES, default=0)
    Mobile = models.CharField(db_column='Mobile', max_length=50)
    OriginalID = models.IntegerField(db_column='OriginalID', blank=True, null=True)

    class Meta(BaseModel.Meta):
        managed = False
        db_table = 'UserInfo'

    def __str__(self):
        return f'{self.FirstName} {self.LastName}'

    def username(self):
        return self.__str__()


class BookingStatusIDInfo(models.Model):
    StatusID = models.SmallIntegerField(db_column='StatusID', blank=True, null=True, unique=True)
    StatusName = models.CharField(db_column='StatusName', max_length=30, blank=True, null=True)
    Cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BookingStatusIDInfo'


class DepartmentIDInfo(models.Model):
    DeptName = models.CharField(db_column='DeptName', max_length=30, blank=True, null=True)
    CreatedByID = models.CharField(db_column='CreatedByID', max_length=32, blank=True, null=True)
    CreatedAt = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    UpdatedByID = models.CharField(db_column='UpdatedByID', max_length=32, blank=True, null=True)
    UpdatedAt = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    OriginalDeptID = models.IntegerField(db_column='OriginalDeptID')
    Cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DepartmentIDInfo'


class FuelTypeIDInfo(models.Model):
    FuelName = models.CharField(db_column='FuelName', max_length=30, blank=True, null=True)
    Cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FuelTypeIDInfo'


class Infringement(BaseModel):
    InfringementNumber = models.CharField(db_column='InfringementNumber', max_length=30, unique=True)
    PlateNumber = models.CharField(db_column='PlateNumber', max_length=30)
    Amount = models.FloatField(db_column='Amount', blank=True, null=True)
    Date = models.DateTimeField(db_column='Date', blank=True, null=True)
    UserID = models.CharField(db_column='UserID', max_length=32, blank=True, null=True)
    PaidDate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)
    OriginalID = models.IntegerField(db_column='OriginalID', blank=True, null=True)
    Status = models.SmallIntegerField(db_column='Status', choices=enums.INFRINGEMENT_STATUS_CHOICES)

    class Meta(BaseModel.Meta):
        managed = False
        db_table = 'Infringement'

    def user_name(self):
        user = UserInfo.objects.with_deleted().filter(UserID=self.UserID).first()
        return user and user.username() or enums.MSG_NOT_FOUND


class JobIDInfo(BaseModel):
    JobAbbreviation = models.CharField(db_column='JobAbbreviation', max_length=30, blank=True, null=True)
    JobName = models.CharField(db_column='JobName', max_length=30, blank=True, null=True)
    Status = models.SmallIntegerField(db_column='Status', choices=enums.JOBIDINFO_STATUS_CHOICES, default=1)
    OriginalJobCodeID = models.IntegerField(db_column='OriginalJobCodeID', blank=True, null=True)
    objects = CommonManager()

    class Meta(BaseModel.Meta):
        managed = False
        db_table = 'JobIDInfo'


def my_custom_sql(query, params):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        # row = cursor.fetchone()

    # return row


class ServiceForm(BaseModel):
    SN = models.CharField(db_column='SN', max_length=25, editable=False)
    PlateNumber = models.CharField(db_column='PlateNumber', max_length=30)
    ServiceName = models.CharField(db_column='ServiceName', max_length=600)
    WorkshopID = models.CharField(db_column='WorkshopID', max_length=32)
    ServicePrice = models.FloatField(db_column='ServicePrice')
    StartDate = models.DateTimeField(db_column='StartDate')
    EndDate = models.DateTimeField(db_column='EndDate')
    Status = models.SmallIntegerField(db_column='Status', choices=enums.SERVICE_STATUS_CHOICES, default=0)
    OriginalID = models.IntegerField(db_column='OriginalID', blank=True, null=True)

    class Meta(BaseModel.Meta):
        managed = False
        db_table = 'ServiceForm'

    def workshop_name(self):
        workshop = WorkshopInfo.objects.with_deleted().filter(WorkshopID=self.WorkshopID).first()
        return workshop and workshop.WorkshopName or enums.MSG_NOT_FOUND


class TransmissionTypeIDInfo(models.Model):
    TransmissionType = models.CharField(db_column='TransmissionType', max_length=30, blank=True, null=True)
    Cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TransmissionTypeIDInfo'


class VehicleBooking(BaseModel):
    SN = models.CharField(db_column='SN', max_length=26, editable=False)
    BookingStartAt = models.DateTimeField(db_column='BookingStartAt', blank=True, null=True)
    BookingEndAt = models.DateTimeField(db_column='BookingEndAt', blank=True, null=True)
    DepartmentID = models.CharField(db_column='DepartmentID', max_length=50, blank=True, null=True)
    JobCodeID = models.IntegerField(db_column='JobCodeID', blank=True, null=True)
    UserID = models.CharField(db_column='UserID', max_length=32, blank=True, null=True)
    VehicleID = models.CharField(db_column='VehicleID', max_length=32, blank=True, null=True)
    BookingReason = models.CharField(db_column='BookingReason', max_length=1200, blank=True, null=True)
    BookingNotes = models.CharField(db_column='BookingNotes', max_length=1200, blank=True, null=True)
    AdminNotes = models.CharField(db_column='AdminNotes', max_length=1200, blank=True, null=True)
    MaintenanceBooking = models.CharField(db_column='MaintenanceBooking', max_length=1200, blank=True, null=True)
    StartedMileage = models.FloatField(db_column='StartedMileage', blank=True, null=True)
    ReturnedMileage = models.FloatField(db_column='ReturnedMileage', blank=True, null=True)
    ReturnedDate = models.DateTimeField(db_column='ReturnedDate', blank=True, null=True)
    ReturnNote = models.CharField(db_column='ReturnNote', max_length=1200, blank=True, null=True)
    Clean = models.SmallIntegerField(db_column='Clean', blank=True, null=True)
    DamageInfo = models.CharField(db_column='DamageInfo', max_length=1200, blank=True, null=True)
    Image = models.CharField(db_column='Image', max_length=200, blank=True, null=True)
    Status = models.ForeignKey('BookingStatusIDInfo', db_column='Status', on_delete=models.PROTECT, default=0,
                               to_field='StatusID')
    OriginalID = models.IntegerField(db_column='OriginalID', blank=True, null=True)

    class Meta(BaseModel.Meta):
        managed = False
        db_table = 'VehicleBooking'


class VehicleInfo(BaseModel):
    # VehicleID = models.CharField(db_column='VehicleID', max_length=50)
    VehicleID = models.UUIDField(db_column='VehicleID', max_length=50, default=uuid.uuid4, editable=False)
    PlateNumber = models.CharField(db_column='PlateNumber', max_length=30, unique=True)
    LastKnownOdo = models.FloatField(db_column='LastKnownOdo', blank=True, null=True)
    LastOdo = models.FloatField(db_column='LastOdo', blank=True, null=True)
    MFGDate = models.IntegerField(db_column='MFGDate', blank=True, null=True)
    Manufacturer = models.CharField(db_column='Manufacturer', max_length=30, blank=True, null=True)
    Model = models.CharField(db_column='Model', max_length=30, blank=True, null=True)
    Color = models.CharField(db_column='Color', max_length=30, blank=True, null=True)
    TransmissionTypeID = models.ForeignKey('TransmissionTypeIDInfo', db_column='TransmissionTypeID', blank=True,
                                           null=True, on_delete=models.PROTECT)
    VehicleTypeID = models.ForeignKey('VehicleTypeIDInfo', db_column='VehicleTypeID', blank=True, null=True,
                                      on_delete=models.PROTECT)
    AvailableKm = models.CharField(db_column='AvailableKm', max_length=50, blank=True, null=True)
    DepartmentID = models.CharField(db_column='DepartmentID', max_length=50, blank=True, null=True)
    FuelTypeID = models.ForeignKey('FuelTypeIDInfo', db_column='FuelTypeID', blank=True, null=True,
                                   on_delete=models.PROTECT)
    WoFExpDate = models.DateTimeField(db_column='WoFExpDate', blank=True, null=True)
    RegoExpDate = models.DateTimeField(db_column='RegoExpDate', blank=True, null=True)
    OriginalID = models.IntegerField(db_column='OriginalID', blank=True, null=True)
    Status = models.SmallIntegerField(db_column='Status', choices=enums.VEHICLE_STATUS_CHOICES, default=1)

    class Meta(BaseModel.Meta):
        managed = False
        db_table = 'VehicleInfo'


class VehicleTypeIDInfo(models.Model):
    VehicleTypename = models.CharField(db_column='VehicleTypename', max_length=30, blank=True, null=True)
    Cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleTypeIDInfo'


class WorkshopInfo(BaseModel):
    WorkshopID = models.UUIDField(db_column='WorkshopID', max_length=50, default=uuid.uuid4, editable=False)
    WorkshopName = models.CharField(db_column='WorkshopName', max_length=60)
    Address = models.CharField(db_column='Address', max_length=600, blank=True, null=True)
    ContactPerson = models.CharField(db_column='ContactPerson', max_length=30, blank=True, null=True)
    ContactPhone = models.CharField(db_column='ContactPhone', max_length=60, blank=True, null=True)
    Email = models.CharField(db_column='Email', max_length=60, blank=True, null=True)
    Note = models.CharField(db_column='Note', max_length=1200, blank=True, null=True)
    OriginalID = models.IntegerField(db_column='OriginalID', blank=True, null=True)

    class Meta(BaseModel.Meta):
        managed = False
        db_table = 'WorkshopInfo'

    def __str__(self):
        return self.WorkshopName


class UserRoleInfo(models.Model):
    RoleID = models.PositiveSmallIntegerField(db_column='RoleID')
    RoleDescription = models.CharField(db_column='RoleDescription', max_length=30, blank=True)
    CreatedByID = models.CharField(db_column='CreatedByID', max_length=50, blank=True, null=True, editable=False)
    CreatedAt = models.DateTimeField(db_column='CreatedAt', auto_now_add=True, editable=False)
    UpdatedByID = models.CharField(db_column='UpdatedByID', max_length=50, blank=True, null=True, editable=False)
    UpdatedAt = models.DateTimeField(db_column='UpdatedAt', auto_now=True, editable=False)
    Cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserRoleInfo'


class LicenseClassInfo(models.Model):
    ClassID = models.CharField(db_column='ClassID', max_length=30)
    LicenseClass = models.CharField(db_column='LicenseClass', max_length=200, blank=True)
    CreatedByID = models.CharField(db_column='CreatedByID', max_length=50, blank=True, null=True, editable=False)
    CreatedAt = models.DateTimeField(db_column='CreatedAt', auto_now_add=True, editable=False)
    UpdatedByID = models.CharField(db_column='UpdatedByID', max_length=50, blank=True, null=True, editable=False)
    UpdatedAt = models.DateTimeField(db_column='UpdatedAt', auto_now=True, editable=False)
    Cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LicenseClassInfo'
