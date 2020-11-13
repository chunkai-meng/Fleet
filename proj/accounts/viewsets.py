from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api_base import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.GenericViewSet):
    queryset = UserProfile.objects.all().order_by('username')
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['get'], detail=False, permission_classes=([IsAuthenticated]))
    def me(self, request):
        """
        Get current user detail
        """
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

