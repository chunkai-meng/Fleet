from rest_framework import serializers
from ..base_serializers import DynamicFieldsModelSerializer
from ..models import VehicleBooking, VehicleInfo
from .. import enums


class VehicleBookingSerializer(DynamicFieldsModelSerializer):
    class Meta(DynamicFieldsModelSerializer.Meta):
        model = VehicleBooking

    def validate(self, attrs):
        v_id = attrs.get('VehicleID', '')
        vehicle = VehicleInfo.objects.get_or_none(VehicleID=v_id)
        started_mileage = vehicle and vehicle.LastOdo or 0
        attrs['StartedMileage'] = started_mileage
        return attrs
