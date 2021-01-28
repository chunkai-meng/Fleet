from collections import OrderedDict

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from fleet.models import UserInfo
from .permissions import IsFleetUser


class MyPageNumberPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('Count', self.page.paginator.count),
            ('Next', self.get_next_link()),
            ('Previous', self.get_previous_link()),
            ('Results', data)
        ]))


class LargeResultsSetPagination(MyPageNumberPagination):
    page_size = 64
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StandardResultsSetPagination(MyPageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100  # ?page_size=100&page=3 自定义page size 不超过100


class BaseViewSetMixin(object):
    """
    Ensure the models are updated with the requesting user.
    """
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsFleetUser,)
    serializer_action_classes = {}

    def get_serializer_class(self, *args, **kwargs):
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()

    def perform_create(self, serializer):
        """Ensure we have the authorized user for ownership."""
        # user = UserInfo.objects.get(SAMAccountName=self.request.user.sam_account_name)
        user = self.get_current_user(self.request)
        serializer.save(CreatedByID=user.UserID)

    def perform_update(self, serializer):
        """Ensure we have the authorized user for ownership."""
        user = self.get_current_user(self.request)
        serializer.save(UpdatedByID=user.UserID)

    def get_serializer(self, *args, **kwargs):
        try:
            fields = self.serializer_fields[self.action]
            return super().get_serializer(fields=fields, *args, **kwargs)
        except(KeyError, AttributeError):
            return super().get_serializer(*args, **kwargs)

    def get_current_user(self, request):
        sam_account_name = request.user.sam_account_name
        current_user = UserInfo.objects.get_or_none(SAMAccountName=sam_account_name)
        return current_user

    def create(self, request, *args, **kwargs):
        if self.lookup_field == 'SN':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            new_obj_id = serializer.data['id']
            new_obj = self.queryset.get(id=new_obj_id)

            serializer = self.get_serializer(new_obj, many=False)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        else:
            return super().create(request, *args, **kwargs)
