# Generated by Django 3.0.11 on 2020-11-17 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(db_column='UserID', max_length=50)),
                ('firstname', models.CharField(db_column='FirstName', max_length=50)),
                ('lastname', models.CharField(db_column='LastName', max_length=50)),
                ('driver_license', models.CharField(blank=True, db_column='DriverLicense', max_length=50, null=True)),
                ('email_address', models.CharField(blank=True, db_column='EmailAddress', max_length=50, null=True)),
                ('department_id', models.CharField(blank=True, db_column='DepartmentID', max_length=50, null=True)),
                ('license_class', models.CharField(blank=True, db_column='LicenseClass', max_length=30, null=True)),
                ('license_expiry_date', models.DateTimeField(blank=True, db_column='LicenseExpiryDate', null=True)),
                ('role', models.SmallIntegerField(blank=True, db_column='Role', null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('mobile', models.CharField(blank=True, db_column='Mobile', max_length=50, null=True)),
                ('created_by_id', models.CharField(blank=True, db_column='CreatedByID', max_length=32, null=True)),
                ('created_at', models.DateTimeField(blank=True, db_column='CreatedAt', null=True)),
                ('updated_by_id', models.CharField(blank=True, db_column='UpdatedByID', max_length=32, null=True)),
                ('updated_at', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('original_id', models.IntegerField(blank=True, db_column='OriginalID', null=True)),
                ('cdate', models.DateTimeField(blank=True, db_column='Cdate', null=True)),
            ],
            options={
                'db_table': 'UserInfo',
                'managed': False,
            },
        ),
    ]