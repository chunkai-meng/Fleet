from rest_framework.response import Response
from rest_framework import mixins, status
from ..serializers.service_form_serializers import ServiceFormSerializer
from ..models import ServiceForm
from ..base_viewsets import BaseViewSetMixin
from api_base import viewsets


class ServiceFormViewSet(BaseViewSetMixin,
                         mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin,
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        new_obj_id = serializer.data['id']
        new_obj = self.queryset.get(id=new_obj_id)

        serializer = self.get_serializer(new_obj, many=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        a = serializer.is_valid(raise_exception=True)
        print(a, serializer)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
