from rest_framework import serializers
from ..base_serializers import DynamicFieldsModelSerializer
from ..models import VehicleInfo, DepartmentIDInfo


class VehicleInfoSerializer(DynamicFieldsModelSerializer):
    CreatedBy = serializers.ReadOnlyField(source='created_by')
    DepartmentName = serializers.SerializerMethodField()

    class Meta(DynamicFieldsModelSerializer.Meta):
        model = VehicleInfo

    def get_DepartmentName(self, obj):
        if obj.DepartmentID:
            department_id_list = obj.DepartmentID.replace(' ', '').split(',')
            departments = DepartmentIDInfo.objects.filter(id__in=department_id_list)
            department_string = ','.join([str(d.DeptName) for d in departments])
        else:
            department_string = ''
        return department_string
