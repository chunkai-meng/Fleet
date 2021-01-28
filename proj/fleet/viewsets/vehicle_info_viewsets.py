from rest_framework import mixins, exceptions
from rest_framework.decorators import action
from datetime import datetime, timedelta
from api_base import viewsets
from ..base_viewsets import BaseViewSetMixin
from ..serializers.vehicle_info_serializers import VehicleInfoSerializer
from ..models import VehicleInfo, UserInfo
from .. import enums
from django.db.models import Q
from ..utils import has_common_member

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
            <tr><td class="parameter-name"><code>use_id</code></td><td>Retrieve vehicles from relevant pool</td></tr>
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
                      'AvailableKm', 'CreatedBy', 'DepartmentName', 'DepartmentID',
                      'FuelType', 'MFGDate',
                      'Odo', 'PlateNumber', 'TransmissionType', 'VehicleID', 'VehicleTypeName', 'VehicleModel',
                      'WoFExpDate', 'RegoExpDate', 'WoFDue', 'RegoDue', 'Color',
                      'Location', 'Longitude', 'Latitude', 'CreatedByID')
    serializer_fields = {
        'list': default_fields,
        'retrieve': default_fields,
    }
    lookup_field = 'VehicleID'

    def perform_destroy(self, instance):
        if int(instance.Status) == enums.VEHICLE_STATUS_AVAILABLE:
            instance.delete()
        else:
            raise exceptions.ValidationError('Deletion failed, this vehicle is not available (booked/deleted)')

    def get_queryset(self):
        queryset = super().get_queryset().select_related('FuelTypeID', 'VehicleTypeID', 'TransmissionTypeID')
        v_type = self.request.query_params.get('v_type', None)
        t_type = self.request.query_params.get('t_type', None)
        user_id = self.request.query_params.get('user_id', None)

        if v_type:
            type_ids = v_type.replace(' ', '').split(',')
            queryset = queryset.filter(VehicleTypeID__in=type_ids)
        if t_type:
            type_ids = t_type.replace(' ', '').split(',')
            queryset = queryset.filter(TransmissionTypeID__in=type_ids)

        if user_id:
            try:
                user = UserInfo.objects.get(UserID=user_id)
            except UserInfo.DoesNotExist:
                raise exceptions.NotFound('user_id not found')
            user_department_id_list = user.DepartmentID.replace(' ', '').split(',')
            all_vehicles = queryset.all().values('id', 'DepartmentID')
            not_in_pool_vehicle_ids = []
            for v in all_vehicles:
                vehicle_department_id_list = v['DepartmentID'].replace(' ', '').split(',')
                if not has_common_member(user_department_id_list, vehicle_department_id_list):
                    not_in_pool_vehicle_ids.append(v['id'])
            queryset = queryset.exclude(id__in=not_in_pool_vehicle_ids)

        # if user_id:
        #     user = UserInfo.objects.get(UserID=user_id)
        #     user_department_id_list = user.DepartmentID.replace(' ', '').split(',')
        #     all_vehicles = queryset.all()
        #     pool = queryset.none()
        #     for i in user_department_id_list:
        #         id_startswith = Q(DepartmentID__startswith=i + ',')
        #         id_in_middle = Q(DepartmentID__contains=',' + i + ',')
        #         id_endswith = i + ','
        #         pool = pool | queryset.filter(DepartmentID__contains=id_in_middle)
        #     queryset = pool

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
