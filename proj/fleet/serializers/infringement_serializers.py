from rest_framework import serializers
from ..base_serializers import DynamicFieldsModelSerializer
from ..models import Infringement, VehicleInfo
from .. import enums


class InfringementSerializer(DynamicFieldsModelSerializer):
    UserName = serializers.ReadOnlyField(source='user_name')
    CreatedBy = serializers.ReadOnlyField(source='created_by')

    class Meta(DynamicFieldsModelSerializer.Meta):
        model = Infringement
        fields = '__all__'

    def validate_PlateNumber(self, value):
        if not VehicleInfo.objects.filter(PlateNumber=value).exists():
            raise serializers.ValidationError("PlateNumber not found")
        return value

    def validate(self, attrs):
        if attrs.get('Status') == enums.INFRINGEMENT_STATUS_PAID and not attrs.get('PaidDate', None):
            raise serializers.ValidationError('PaidDate field required when status==1')
        return super(InfringementSerializer, self).validate(attrs)
