from rest_framework import serializers
from ..models import UserInfo
# from ..utils import uppercase_field_name
from ..base_serializers import DynamicFieldsModelSerializer
from accounts.models import UserProfile


class UserInfoSerializer(DynamicFieldsModelSerializer):
    total = serializers.SerializerMethodField()
    Username = serializers.ReadOnlyField(source='username')

    class Meta:
        model = UserInfo
        fields = ('id', 'UserID', 'SAMAccountName',
                  'CreatedByID', 'DepartmentID', 'DriverLicense', 'EmailAddress', 'LicenseClass', 'LicenseExpiryDate',
                  'Mobile', 'Role', 'Username', 'total',
                  )

    def get_total(self, obj):
        return self.Meta.model.objects.count()

    def validate(self, data):
        if 'SAMAccountName' in data:
            sam_account_name = data['SAMAccountName']
            staff = UserProfile.objects.filter(sam_account_name=sam_account_name).first()
            if staff is None:
                raise serializers.ValidationError("SAMAccountName not exist in Staff")
            else:
                data['FirstName'] = staff.first_name
                data['LastName'] = staff.last_name
                data['EmailAddress'] = staff.email
        return data
