from rest_framework import serializers
from ..models import WorkshopInfo
from ..base_serializers import DynamicFieldsModelSerializer


class WorkshopInfoSerializer(DynamicFieldsModelSerializer):
    CreatedBy = serializers.ReadOnlyField(source='created_by')

    class Meta:
        model = WorkshopInfo
        fields = ('id', 'WorkshopID', 'WorkshopName', 'Address', 'ContactPerson',
                  'ContactPhone', 'Email', 'Note', 'CreatedAt', 'CreatedBy', 'CreatedByID')

    # def validate_PlateNumber(self, value):
    #     if not VehicleInfo.objects.filter(PlateNumber=value).exists():
    #         raise serializers.ValidationError("PlateNumber not found")
    #     return value
    #
    # def validate_WorkshopID(self, value):
    #     if not WorkshopInfo.objects.filter(WorkshopID=value).exists():
    #         raise serializers.ValidationError("PlateNumber not found")
    #     return value
