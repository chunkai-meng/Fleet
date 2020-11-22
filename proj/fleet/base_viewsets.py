from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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
    permission_classes = (IsAuthenticated,)
    serializer_action_classes = {}

    def get_serializer_class(self, *args, **kwargs):
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()

    # def perform_create(self, serializer):
    #     """Ensure we have the authorized user for ownership."""
    #     serializer.save(created_by=self.request.user,
    #                     updated_by=self.request.user)
    #
    # def perform_update(self, serializer):
    #     """Ensure we have the authorized user for ownership."""
    #     serializer.save(updated_by=self.request.user)
    #
