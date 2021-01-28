from rest_framework import serializers
from ..base_serializers import DynamicFieldsModelSerializer
from ..models import VehicleBooking, VehicleInfo, JobIDInfo
from .. import enums
from .job_id_serializers import JobIDInfoSerializer


class VehicleBookingSerializer(DynamicFieldsModelSerializer):
    StatusName = serializers.ReadOnlyField(source='Status.StatusName')
    PlateNumber = serializers.SerializerMethodField()
    JobName = serializers.SerializerMethodField()

    # UserName

    class Meta(DynamicFieldsModelSerializer.Meta):
        model = VehicleBooking

    def validate(self, attrs):
        v_id = attrs.get('VehicleID', '')
        vehicle = VehicleInfo.objects.get_or_none(VehicleID=v_id)
        if vehicle.Status == 1 and self.instance is None:
            vehicle.Status = 0
            vehicle.save()
        elif vehicle.Status == 0 and self.instance is None:
            raise serializers.ValidationError("This vehicle has been booked")
        started_mileage = vehicle and vehicle.LastOdo or 0
        attrs['StartedMileage'] = started_mileage
        return attrs

    def get_PlateNumber(self, obj):
        v = VehicleInfo.objects.get_or_none(VehicleID=obj.VehicleID)
        if isinstance(v, VehicleInfo):
            return v.PlateNumber
        else:
            return ''

    def get_JobName(self, obj):
        try:
            return obj.JobCodeID.JobName
        except JobIDInfo.DoesNotExist:
            return ''
