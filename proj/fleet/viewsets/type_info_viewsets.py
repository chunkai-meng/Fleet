from rest_framework import mixins
from ..models import FuelTypeIDInfo, VehicleTypeIDInfo, DepartmentIDInfo
from ..base_viewsets import BaseViewSetMixin
from ..serializers.type_info_serializers import FuelTypeSerializer, VehicleTypeSerializer, DepartmentTypeSerializer
from api_base import viewsets


class FuelTypeViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = FuelTypeSerializer
    queryset = FuelTypeIDInfo.objects.all()


class VehicleTypeViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = VehicleTypeSerializer
    queryset = VehicleTypeIDInfo.objects.all()


class DepartmentViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = DepartmentTypeSerializer
    queryset = DepartmentIDInfo.objects.all()
