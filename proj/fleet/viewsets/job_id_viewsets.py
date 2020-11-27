from rest_framework import mixins
from ..models import JobIDInfo
from ..base_viewsets import BaseViewSetMixin
from ..serializers.job_id_serializers import JobIDInfoSerializer
from api_base import viewsets


class JobIDInfoViewSet(BaseViewSetMixin,
                       mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = JobIDInfoSerializer
    queryset = JobIDInfo.objects.all()
