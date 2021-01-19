from rest_framework import serializers
from ..base_serializers import DynamicFieldsModelSerializer
from ..models import FuelTypeIDInfo, VehicleTypeIDInfo, DepartmentIDInfo


class FuelTypeSerializer(DynamicFieldsModelSerializer):
    class Meta(DynamicFieldsModelSerializer.Meta):
        model = FuelTypeIDInfo


class VehicleTypeSerializer(DynamicFieldsModelSerializer):
    class Meta(DynamicFieldsModelSerializer.Meta):
        model = VehicleTypeIDInfo


class DepartmentTypeSerializer(DynamicFieldsModelSerializer):
    class Meta(DynamicFieldsModelSerializer.Meta):
        model = DepartmentIDInfo
