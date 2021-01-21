from rest_framework import serializers
from ..models import UserInfo, DepartmentIDInfo
from ..base_serializers import DynamicFieldsModelSerializer
from accounts.models import UserProfile


class UserInfoSerializer(DynamicFieldsModelSerializer):
    UserName = serializers.ReadOnlyField(source='username')
    DepartmentName = serializers.SerializerMethodField()

    class Meta:
        model = UserInfo
        fields = ('id', 'UserID', 'SAMAccountName', 'DepartmentName',
                  'CreatedByID', 'DriverLicense', 'EmailAddress', 'LicenseClass', 'LicenseExpiryDate',
                  'Mobile', 'Role', 'UserName',
                  )

    def validate(self, data):
        if self.context['view'].action == 'create' and 'SAMAccountName' in data:
            sam_account_name = data['SAMAccountName']
        else:
            data.pop('SAMAccountName', None)
            sam_account_name = self.instance.SAMAccountName

        staff = UserProfile.objects.filter(sam_account_name=sam_account_name).first()
        if staff is None:
            raise serializers.ValidationError("SAMAccountName not exist in accounts_userprofile, please contact admin")
        else:
            data['FirstName'] = staff.first_name
            data['LastName'] = staff.last_name
            data['EmailAddress'] = staff.email
        return data

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        staff = UserProfile.objects.filter(sam_account_name=instance.SAMAccountName).first()
        staff.user_info = instance
        staff.save()
        return instance

    def get_DepartmentName(self, obj):
        if obj.DepartmentID:
            department_id_list = obj.DepartmentID.replace(' ', '').split(',')
            departments = DepartmentIDInfo.objects.filter(id__in=department_id_list)
            department_string = ','.join([str(d.DeptName) for d in departments])
        else:
            department_string = ''
        return department_string
