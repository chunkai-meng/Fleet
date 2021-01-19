from rest_framework import serializers
from ..base_serializers import DynamicFieldsModelSerializer
from ..models import FuelTypeIDInfo, VehicleTypeIDInfo, DepartmentIDInfo, UserRoleInfo, LicenseClassInfo


class FuelTypeSerializer(DynamicFieldsModelSerializer):
    class Meta(DynamicFieldsModelSerializer.Meta):
        model = FuelTypeIDInfo


class VehicleTypeSerializer(DynamicFieldsModelSerializer):
    class Meta(DynamicFieldsModelSerializer.Meta):
        model = VehicleTypeIDInfo


class DepartmentTypeSerializer(DynamicFieldsModelSerializer):
    class Meta(DynamicFieldsModelSerializer.Meta):
        model = DepartmentIDInfo


class UserRoleInfoSerializer(DynamicFieldsModelSerializer):
    class Meta(DynamicFieldsModelSerializer.Meta):
        model = UserRoleInfo


class LicenseClassInfoSerializer(DynamicFieldsModelSerializer):
    class Meta(DynamicFieldsModelSerializer.Meta):
        model = LicenseClassInfo
