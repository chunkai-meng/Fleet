from rest_framework import serializers
from ..models import WorkshopInfo
from ..base_serializers import DynamicFieldsModelSerializer


class WorkshopInfoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = WorkshopInfo
        fields = ('id', 'SN', 'WorkshopID', 'WorkshopName', 'PlateNumber', 'ServiceName',
                  'ServicePrice', 'StartDate', 'EndDate', 'CreatedBy', 'total')

    # def validate_PlateNumber(self, value):
    #     if not VehicleInfo.objects.filter(PlateNumber=value).exists():
    #         raise serializers.ValidationError("PlateNumber not found")
    #     return value
    #
    # def validate_WorkshopID(self, value):
    #     if not WorkshopInfo.objects.filter(WorkshopID=value).exists():
    #         raise serializers.ValidationError("PlateNumber not found")
    #     return value
