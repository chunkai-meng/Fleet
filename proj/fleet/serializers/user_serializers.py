from rest_framework import serializers
from ..models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = UserInfo
        fields = ('created_by_id', 'department_id', 'driver_license',
                  'email_address', 'license_class', 'license_expiry_date',
                  'mobile', 'role', 'username', 'total')

    def get_total(self, obj):
        return UserInfo.objects.count()
