from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


# LIST_MAX_NUMBER = 10000
# import redis
# r = redis.StrictRedis(host=settings.REDIS_HOST,
#                       port=settings.REDIS_PORT, db=settings.REDIS_DB)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 64
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100  # ?page_size=100&page=3 自定义page size 不超过100


class BaseModelMixin(object):
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

    def perform_create(self, serializer):
        """Ensure we have the authorized user for ownership."""
        serializer.save(created_by=self.request.user,
                        updated_by=self.request.user)

    def perform_update(self, serializer):
        """Ensure we have the authorized user for ownership."""
        serializer.save(updated_by=self.request.user)

    @action(methods=['get'], detail=False, url_path='count', url_name='count')
    def count(self, request):
        count = self.get_queryset().count()
        return Response({'count': count})
