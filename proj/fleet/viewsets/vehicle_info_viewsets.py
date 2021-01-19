from rest_framework import mixins
from rest_framework.decorators import action
from datetime import datetime, timedelta
from api_base import viewsets
from ..base_viewsets import BaseViewSetMixin
from ..serializers.vehicle_info_serializers import VehicleInfoSerializer
from ..models import VehicleInfo
from .. import enums
from django.db.models import Q

now = datetime.now()
date_out = now + timedelta(days=enums.COMMON_EXPIRED_DAYS)
wof_expired = Q(WoFExpDate__lte=date_out)
rego_expired = Q(RegoExpDate__lte=date_out)
wof_reminder = Q(WoFExpDate__range=[now, date_out])
rego_reminder = Q(RegoExpDate__range=[now, date_out])


class VehicleInfoViewSet(BaseViewSetMixin,
                         mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    """
    list:
    **这里有几处跟Sandy不一样的地方：**

    不提供 Availability 字段：因为跟status重复，（Status: 0:booked; 1=available; -1=deleted）

    不提供 VehicleInfo字段：因其是 Manufacturer 和 Model 的拼接，没有必要也不应该，在此分别提供两个原始字段

    不提供 Odo字段: 是 LastKnownOdo 和 LastOdo 字段的拼接，没有必要也不应该，在此分别提供两个原是字段

    ### Search

    <span class="label label-primary">GET</span> `/api/vehicle-info?v_type=1,2&t_type=1,3`
    <table class="parameters table table-bordered table-striped">
        <thead>
            <tr><th>Parameter</th><th>Description</th></tr>
        </thead>
        <tbody>
            <tr><td class="parameter-name"><code>v_type</code></td><td>VehicleTypeIDs</td></tr>
            <tr><td class="parameter-name"><code>t_type</code></td><td>TransmissionTypeIDs</td></tr>
        </tbody>
    </table>

    create:
    All Fields are **required** (所有字段必填)

    wof_due_list:
    list vehicles that WofExpired within 30 days

    rego_due_list:
    list vehicles that RegoExpired within 30 days

    due_list:
    list all vehicles that with due WoF/Rego
    """

    serializer_class = VehicleInfoSerializer
    queryset = VehicleInfo.objects.all()
    default_fields = ('id',
                      'Status', 'LastKnownOdo', 'LastOdo', 'Manufacturer', 'Model',
                      'AvailableKm', 'CreatedBy', 'DepartmentName', 'FuelType', 'MFGDate',
                      'Odo', 'PlateNumber', 'TransmissionType', 'VehicleID', 'VehicleTypeID', 'VehicleModel',
                      'WoFExpDate',
                      'RegoExpDate', 'WoFDue', 'RegoDue', 'Color')
    serializer_fields = {
        'list': default_fields,
        'retrieve': default_fields,
    }
    lookup_field = 'VehicleID'

    def get_queryset(self):
        queryset = super().get_queryset()
        v_type = self.request.query_params.get('v_type', None)
        t_type = self.request.query_params.get('t_type', None)
        if v_type:
            type_ids = v_type.replace(' ', '').split(',')
            queryset = queryset.filter(VehicleTypeID__in=type_ids)
        if t_type:
            type_ids = t_type.replace(' ', '').split(',')
            queryset = queryset.filter(TransmissionTypeID__in=type_ids)
        return queryset

    @action(detail=False, methods=['get'], url_path='wof-due')
    def wof_due_list(self, request):
        queryset = self.get_queryset().filter(wof_reminder)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['get'], url_path='ergo-due')
    def rego_due_list(self, request):
        queryset = self.get_queryset().filter(rego_reminder)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['get'], url_path='due')
    def due_list(self, request):
        queryset = self.get_queryset().filter(wof_expired | rego_expired)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
