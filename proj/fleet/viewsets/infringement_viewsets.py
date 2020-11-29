from rest_framework import mixins
from api_base import viewsets
from ..base_viewsets import BaseViewSetMixin
from ..serializers.infringement_serializers import InfringementSerializer
from ..models import Infringement


class InfringementViewSets(BaseViewSetMixin,
                           mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = InfringementSerializer
    queryset = Infringement.objects.all()
    serializer_fields = {
        'list': ('Amount', 'CreatedByID', 'Date', 'InfringementNumber', 'PaidDate',
                 'PlateNumber', 'Status', 'UserID', 'UserName'),
        'retrieve': ('id', 'Amount', 'CreatedAt', 'CreatedBy', 'CreatedByID', 'Date', 'InfringementNumber', 'PaidDate',
                     'PlateNumber', 'Status', 'UserName')
    }
