from rest_framework.response import Response
from rest_framework import mixins, status
from ..serializers.workshop_info_serializers import WorkshopInfoSerializer
from ..models import WorkshopInfo
from ..base_viewsets import BaseViewSetMixin
from api_base import viewsets


class WorkshopInfoViewSet(BaseViewSetMixin,
                          mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    """
    retrieve:


    list:


    create:
    All Fields are **required** except for **'SN'**
    """

    serializer_class = WorkshopInfoSerializer
    queryset = WorkshopInfo.objects.all()
    lookup_field = 'WorkshopID'

    detail_fields = ('id', 'WorkshopID', 'WorkshopName', 'Address', 'ContactPerson',
                     'ContactPhone', 'Email', 'Note', 'CreatedByID')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, fields=self.detail_fields)
        return Response(serializer.data)
