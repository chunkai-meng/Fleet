from rest_framework import serializers
from ..base_serializers import DynamicFieldsModelSerializer
from ..models import VehicleBooking
from .. import enums


class VehicleBookingSerializer(DynamicFieldsModelSerializer):
    class Meta(DynamicFieldsModelSerializer.Meta):
        model = VehicleBooking
       