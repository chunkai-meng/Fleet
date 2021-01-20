from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from ..serializers.user_info_serializers import UserInfoSerializer
from ..models import UserInfo
from ..base_viewsets import BaseViewSetMixin
from api_base import viewsets
from fleet.permissions import IsAdminUser, IsFleetUser
from accounts.models import UserProfile


class UserInfoViewSet(BaseViewSetMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet, ):
    """
    retrieve:


    list:


    create:
    All Fields are **required** (所有字段必填)
    """

    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()
    lookup_field = 'UserID'
    permission_classes = (IsAuthenticated, IsAdminUser)
