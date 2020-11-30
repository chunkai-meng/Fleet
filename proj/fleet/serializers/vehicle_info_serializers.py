from rest_framework import serializers
from ..base_serializers import DynamicFieldsModelSerializer
from ..models import VehicleInfo, DepartmentIDInfo, FuelTypeIDInfo, TransmissionTypeIDInfo
from datetime import datetime, timedelta
from .. import enums


class VehicleInfoSerializer(DynamicFieldsModelSerializer):
    CreatedBy = serializers.ReadOnlyField(source='created_by')
    DepartmentName = serializers.SerializerMethodField()
    FuelType = serializers.SerializerMethodField()
    # Odo = serializers.SerializerMethodField()
    TransmissionType = serializers.SerializerMethodField()
    WoFRegoDue = serializers.SerializerMethodField()

    # VehicleModel = serializers.SerializerMethodField()

    class Meta(DynamicFieldsModelSerializer.Meta):
        model = VehicleInfo

    def get_DepartmentName(self, obj):
        # NOTE: Sandy的数据库设计不合理，不应该使用关联表，应该使用静态变量或者常量实现。
        if obj.DepartmentID:
            department_id_list = obj.DepartmentID.replace(' ', '').split(',')
            departments = DepartmentIDInfo.objects.filter(id__in=department_id_list)
            department_string = ','.join([str(d.DeptName) for d in departments])
        else:
            department_string = ''
        return department_string

    def get_FuelType(self, obj):
        if obj.FuelTypeID:
            try:
                fuel_type = FuelTypeIDInfo.objects.get(id=obj.FuelTypeID)
                fuel_name = fuel_type.FuelName
            except FuelTypeIDInfo.DoesNotExist:
                fuel_name = ''
        else:
            fuel_name = ''
        return fuel_name

    # def get_Odo(self, obj):
    #     # TODO: TBD
    #     return obj.LastOdo

    def get_TransmissionType(self, obj):
        # NOTE: Sandy的数据库设计不合理，不应该使用关联表，应该使用静态变量或者常量实现。
        if obj.TransmissionTypeID:
            try:
                transmission_type = TransmissionTypeIDInfo.objects.get(id=obj.TransmissionTypeID)
                transmission_type = transmission_type.TransmissionType
            except FuelTypeIDInfo.DoesNotExist:
                transmission_type = ''
        else:
            transmission_type = ''
        return transmission_type

    # def get_VehicleModel(self, obj):
    #     # TODO： 名字不能用VehicleInfo 重名了，需要Sandy改一下
    #     return f'{obj.Manufacturer} {obj.Model}'

    def get_WoFRegoDue(self, obj):
        now = datetime.now()
        out_date = now + timedelta(days=enums.COMMON_EXPIRED_DAYS)
        return obj.WoFExpDate >= out_date or obj.RegoExpDate >= out_date
