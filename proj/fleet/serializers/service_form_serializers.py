from rest_framework import serializers
from ..models import ServiceForm
from ..base_serializers import DynamicFieldsModelSerializer


class ServiceFormSerializer(DynamicFieldsModelSerializer):
    total = serializers.SerializerMethodField()
    CreatedBy = serializers.ReadOnlyField(source='created_by')
    WorkshopName = serializers.ReadOnlyField(source='workshop_name')

    class Meta:
        model = ServiceForm
        fields = ('CreatedBy', 'EndDate', 'PlateNumber', 'SN', 'ServiceName', 'ServicePrice',
                  'StartDate', 'WorkshopName', 'total')

    def get_total(self, obj):
        return self.Meta.model.objects.count()
