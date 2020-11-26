from rest_framework import serializers
from ..models import ServiceForm, VehicleInfo, WorkshopInfo
from ..base_serializers import DynamicFieldsModelSerializer


class ServiceFormSerializer(DynamicFieldsModelSerializer):
    total = serializers.SerializerMethodField()
    CreatedBy = serializers.ReadOnlyField(source='created_by')
    WorkshopName = serializers.ReadOnlyField(source='workshop_name')

    class Meta:
        model = ServiceForm
        fields = ('id', 'SN', 'WorkshopID', 'WorkshopName', 'PlateNumber', 'ServiceName',
                  'ServicePrice', 'StartDate', 'EndDate', 'CreatedBy', 'total')

    def get_total(self, obj):
        return self.Meta.model.objects.count()

    def validate_PlateNumber(self, value):
        if not VehicleInfo.objects.filter(PlateNumber=value).exists():
            raise serializers.ValidationError("PlateNumber not found")
        return value

    def validate_WorkshopID(self, value):
        if not WorkshopInfo.objects.filter(WorkshopID=value).exists():
            raise serializers.ValidationError("PlateNumber not found")
        return value
