from rest_framework import mixins, status
from ..serializers.service_form_serializers import ServiceFormSerializer
from ..models import ServiceForm
from ..base_viewsets import BaseViewSetMixin
from api_base import viewsets


class ServiceFormViewSet(BaseViewSetMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         viewsets.GenericViewSet, ):
    """
    retrieve:


    list:


    create:
    All Fields are **required** except for **'SN'**
    """

    serializer_class = ServiceFormSerializer
    queryset = ServiceForm.objects.all()
    lookup_field = 'SN'
