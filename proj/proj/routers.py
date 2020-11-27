from rest_framework import routers
from accounts.viewsets import UserProfileViewSet
from fleet.viewsets.user_info_viewsets import UserInfoViewSet
from fleet.viewsets.service_form_viewsets import ServiceFormViewSet
from fleet.viewsets.workshop_info_viewsets import WorkshopInfoViewSet
from fleet.viewsets.job_id_viewsets import JobIDInfoViewSet

router = routers.SimpleRouter()
router.register(r'staffs', UserProfileViewSet, basename='staffs')
router.register(r'user-info', UserInfoViewSet, basename='user_info')
router.register(r'service-form', ServiceFormViewSet, basename='service_form')
router.register(r'workshop-info', WorkshopInfoViewSet, basename='workshop_info')
router.register(r'job-code', JobIDInfoViewSet, basename='job_code')
