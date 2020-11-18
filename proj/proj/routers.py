from rest_framework import routers
from fleet.viewsets.user_viewsets import UserInfoViewSet

router = routers.SimpleRouter()
router.register(r'user-info', UserInfoViewSet, basename='user_info')
