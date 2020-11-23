from rest_framework import routers
from fleet.viewsets.user_info_viewsets import UserInfoViewSet
from fleet.viewsets.service_form_viewsets import ServiceFormViewSet

router = routers.SimpleRouter()
router.register(r'user-info', UserInfoViewSet, basename='user_info')
router.register(r'service-form', ServiceFormViewSet, basename='service_form')
