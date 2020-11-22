from rest_framework import viewsets
from .view import GenericAPIView


class GenericViewSet(viewsets.ViewSetMixin, GenericAPIView):
    pass
