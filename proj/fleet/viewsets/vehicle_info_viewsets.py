from rest_framework import mixins
from api_base import viewsets
from ..base_viewsets import BaseViewSetMixin
from ..serializers.vehicle_info_serializers import VehicleInfoSerializer
from ..models import VehicleInfo


class VehicleInfoViewSet(BaseViewSetMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = VehicleInfoSerializer
    queryset = VehicleInfo.objects.all()
    serializer_fields = {
        'list': ('id',
                 # 'Availability',
                 'AvailableKm', 'CreatedBy', 'DepartmentName', 'FuelType', 'MFGDate',
                 'Odo', 'PlateNumber', 'TransmissionType', 'VehicleID', 'VehicleInfo', 'WoFRegoDue')
    }
