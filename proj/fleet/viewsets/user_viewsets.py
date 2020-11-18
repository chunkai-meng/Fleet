from rest_framework import viewsets
from ..serializers.user_serializers import UserInfoSerializer
from ..models import UserInfo
from ..base_viewsets import BaseViewSetMixin


class UserInfoViewSet(BaseViewSetMixin,
                      viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()
