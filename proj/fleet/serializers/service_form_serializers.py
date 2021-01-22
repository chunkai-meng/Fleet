from rest_framework import serializers
from ..models import ServiceForm, VehicleInfo, WorkshopInfo
from ..base_serializers import DynamicFieldsModelSerializer
from .. import enums


class ServiceFormSerializer(DynamicFieldsModelSerializer):
    CreatedBy = serializers.ReadOnlyField(source='created_by')
    WorkshopName = serializers.ReadOnlyField(source='workshop_name')

    class Meta:
        model = ServiceForm
        fields = ('id', 'SN', 'WorkshopID', 'WorkshopName', 'PlateNumber', 'ServiceName', 'Status',
                  'ServicePrice', 'StartDate', 'EndDate', 'CreatedBy')

    def validate_PlateNumber(self, value):
        if not VehicleInfo.objects.filter(PlateNumber=value).exists():
            raise serializers.ValidationError("PlateNumber not found")
        return value

    def validate_WorkshopID(self, value):
        if not WorkshopInfo.objects.filter(WorkshopID=value).exists():
            raise serializers.ValidationError("PlateNumber not found")
        return value

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        vehicle_pn = instance.PlateNumber
        vehicle = VehicleInfo.objects.get_or_none(PlateNumber=vehicle_pn)
        if instance.Status == enums.SERVICE_STATUS_PROCESSING:
            vehicle.Status = enums.VEHICLE_STATUS_IN_SERVICE
            vehicle.save()
        elif instance.Status == enums.SERVICE_STATUS_COMPLETED:
            vehicle.Status = enums.VEHICLE_STATUS_AVAILABLE
            vehicle.save()
        return instance
