# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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

    def __str__(self):
        return f'{self.lastname}.{self.firstname}'


class BookingStatusIDInfo(models.Model):
    status_id = models.SmallIntegerField(db_column='StatusID', blank=True, null=True)
    status_name = models.CharField(db_column='StatusName', max_length=30, blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BookingStatusIDInfo'


class DepartmentIDInfo(models.Model):
    dept_name = models.CharField(db_column='DeptName', max_length=30, blank=True, null=True)
    created_by_id = models.CharField(db_column='CreatedByID', max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_by_id = models.CharField(db_column='UpdatedByID', max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    original_dept_id = models.IntegerField(db_column='OriginalDeptID')
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DepartmentIDInfo'


class FuelTypeIDInfo(models.Model):
    fuel_name = models.CharField(db_column='FuelName', max_length=30, blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FuelTypeIDInfo'


class Infringement(models.Model):
    infringement_number = models.CharField(db_column='InfringementNumber', max_length=30)
    plate_number = models.CharField(db_column='PlateNumber', max_length=30)
    amount = models.FloatField(db_column='Amount', blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)
    user_id = models.CharField(db_column='UserID', max_length=32, blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)
    paid_date = models.DateTimeField(db_column='PaidDate', blank=True, null=True)
    created_by_id = models.CharField(db_column='CreatedByID', max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_by_id = models.CharField(db_column='UpdatedByID', max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    original_id = models.IntegerField(db_column='OriginalID', blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Infringement'


class JobIDInfo(models.Model):
    job_abbreviation = models.CharField(db_column='JobAbbreviation', max_length=30, blank=True, null=True)
    job_name = models.CharField(db_column='JobName', max_length=30, blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)
    created_by_id = models.CharField(db_column='CreatedByID', max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_by_id = models.CharField(db_column='UpdatedByID', max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    original_job_code_id = models.IntegerField(db_column='OriginalJobCodeID', blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'JobIDInfo'


class ServiceForm(models.Model):
    sn = models.CharField(db_column='SN', max_length=25, blank=True, null=True)
    plate_number = models.CharField(db_column='PlateNumber', max_length=30)
    service_name = models.CharField(db_column='ServiceName', max_length=600, blank=True, null=True)
    workshop_id = models.CharField(db_column='WorkshopID', max_length=32, blank=True, null=True)
    service_price = models.FloatField(db_column='ServicePrice', blank=True, null=True)
    start_date = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    end_date = models.DateTimeField(db_column='EndDate', blank=True, null=True)
    created_by_id = models.CharField(db_column='CreatedByID', max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_by_id = models.CharField(db_column='UpdatedByID', max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    original_id = models.IntegerField(db_column='OriginalID', blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ServiceForm'


class TransmissionTypeIDInfo(models.Model):
    transmission_type = models.CharField(db_column='TransmissionType', max_length=30, blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TransmissionTypeIDInfo'


class VehicleBooking(models.Model):
    sn = models.CharField(db_column='SN', max_length=26, blank=True, null=True)
    booking_start_at = models.DateTimeField(db_column='BookingStartAt', blank=True, null=True)
    booking_end_at = models.DateTimeField(db_column='BookingEndAt', blank=True, null=True)
    department_id = models.CharField(db_column='DepartmentID', max_length=50, blank=True, null=True)
    job_code_id = models.IntegerField(db_column='JobCodeID', blank=True, null=True)
    user_id = models.CharField(db_column='UserID', max_length=32, blank=True, null=True)
    vehicle_id = models.CharField(db_column='VehicleID', max_length=32, blank=True, null=True)
    booking_reason = models.CharField(db_column='BookingReason', max_length=1200, blank=True, null=True)
    booking_notes = models.CharField(db_column='BookingNotes', max_length=1200, blank=True, null=True)
    admin_notes = models.CharField(db_column='AdminNotes', max_length=1200, blank=True, null=True)
    maintenance_booking = models.CharField(db_column='MaintenanceBooking', max_length=1200, blank=True, null=True)
    started_mileage = models.FloatField(db_column='StartedMileage', blank=True, null=True)
    returned_mileage = models.FloatField(db_column='ReturnedMileage', blank=True, null=True)
    returned_date = models.DateTimeField(db_column='ReturnedDate', blank=True, null=True)
    return_note = models.CharField(db_column='ReturnNote', max_length=1200, blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)
    clean = models.SmallIntegerField(db_column='Clean', blank=True, null=True)
    damage_info = models.CharField(db_column='DamageInfo', max_length=1200, blank=True, null=True)
    created_by_id = models.CharField(db_column='CreatedByID', max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_by_id = models.CharField(db_column='UpdatedByID', max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    original_id = models.IntegerField(db_column='OriginalID', blank=True, null=True)
    image = models.CharField(db_column='Image', max_length=200, blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleBooking'


class VehicleInfo(models.Model):
    vehicle_id = models.CharField(db_column='VehicleID', max_length=50)
    plate_number = models.CharField(db_column='PlateNumber', max_length=30)
    last_known_odo = models.FloatField(db_column='LastKnownOdo', blank=True, null=True)
    last_odo = models.FloatField(db_column='LastOdo', blank=True, null=True)
    mfg_date = models.IntegerField(db_column='MFGDate', blank=True, null=True)
    manufacturer = models.CharField(db_column='Manufacturer', max_length=30, blank=True, null=True)
    model = models.CharField(db_column='Model', max_length=30, blank=True, null=True)
    color = models.CharField(db_column='Color', max_length=30, blank=True, null=True)
    transmission_type_id = models.SmallIntegerField(db_column='TransmissionTypeID', blank=True, null=True)
    vehicle_type_id = models.IntegerField(db_column='VehicleTypeID', blank=True, null=True)
    available_km = models.CharField(db_column='AvailableKm', max_length=50, blank=True, null=True)
    department_id = models.CharField(db_column='DepartmentID', max_length=50, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=32, blank=True, null=True)
    fuel_type_id = models.SmallIntegerField(db_column='FuelTypeID', blank=True, null=True)
    wof_exp_date = models.DateTimeField(db_column='WoFExpDate', blank=True, null=True)
    rego_exp_date = models.DateTimeField(db_column='RegoExpDate', blank=True, null=True)
    created_by_id = models.CharField(db_column='CreatedByID', max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_by_id = models.CharField(db_column='UpdatedByID', max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    original_id = models.IntegerField(db_column='OriginalID', blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleInfo'


class VehicleTypeIDInfo(models.Model):
    vehicle_type_name = models.CharField(db_column='VehicleTypename', max_length=30, blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VehicleTypeIDInfo'


class WorkshopInfo(models.Model):
    workshop_id = models.CharField(db_column='WorkshopID', max_length=50)
    workshop_name = models.CharField(db_column='WorkshopName', max_length=60)
    address = models.CharField(db_column='Address', max_length=600, blank=True, null=True)
    contact_person = models.CharField(db_column='ContactPerson', max_length=30, blank=True,
                                      null=True)
    contact_phone = models.CharField(db_column='ContactPhone', max_length=60, blank=True,
                                     null=True)
    email = models.CharField(db_column='Email', max_length=60, blank=True, null=True)
    note = models.CharField(db_column='Note', max_length=1200, blank=True, null=True)
    created_by_id = models.CharField(db_column='CreatedByID', max_length=32, blank=True,
                                     null=True)
    created_at = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)
    updated_by_id = models.CharField(db_column='UpdatedByID', max_length=32, blank=True,
                                     null=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)
    original_id = models.IntegerField(db_column='OriginalID', blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)
    cdate = models.DateTimeField(db_column='Cdate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WorkshopInfo'
