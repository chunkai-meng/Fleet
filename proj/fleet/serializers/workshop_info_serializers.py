from rest_framework import serializers
from ..models import WorkshopInfo
from ..base_serializers import DynamicFieldsModelSerializer


class WorkshopInfoSerializer(DynamicFieldsModelSerializer):
    CreatedBy = serializers.ReadOnlyField(source='created_by')

    class Meta:
        model = WorkshopInfo
        fields = ('id', 'WorkshopID', 'WorkshopName', 'Address', 'ContactPerson',
                  'ContactPhone', 'Email', 'Note', 'CreatedAt', 'CreatedBy', 'CreatedByID')
