from rest_framework import serializers
from ..models import UserInfo
# from ..utils import uppercase_field_name
from ..base_serializers import DynamicFieldsModelSerializer


class UserInfoSerializer(DynamicFieldsModelSerializer):
    total = serializers.SerializerMethodField()
    Username = serializers.ReadOnlyField(source='username')

    class Meta:
        model = UserInfo
        fields = ('CreatedByID', 'DepartmentID', 'DriverLicense', 'EmailAddress', 'LicenseClass', 'LicenseExpiryDate',
                  'Mobile', 'Role', 'Username', 'total', 'UserID', 'id'
                  )

    def get_total(self, obj):
        return self.Meta.model.objects.count()

    # def get_field_names(self, declared_fields, info):
    #     fields = super().get_field_names(declared_fields, info)
    #     # for field in fields:
    #     #     fields
    #     print(uppercase_field_name(fields))
    #     return fields
