from rest_framework import serializers
from ..base_serializers import DynamicFieldsModelSerializer
from ..models import JobIDInfo


class JobIDInfoSerializer(DynamicFieldsModelSerializer):
    CreatedBy = serializers.ReadOnlyField(source='created_by')

    class Meta:
        model = JobIDInfo
        fields = ('id', 'JobName', 'JobAbbreviation', 'Status', 'CreatedBy')
