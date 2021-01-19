from rest_framework import routers
from accounts.viewsets import UserProfileViewSet
from fleet.viewsets.user_info_viewsets import UserInfoViewSet
from fleet.viewsets.service_form_viewsets import ServiceFormViewSet
from fleet.viewsets.workshop_info_viewsets import WorkshopInfoViewSet
from fleet.viewsets.job_id_viewsets import JobIDInfoViewSet
from fleet.viewsets.infringement_viewsets import InfringementViewSets
from fleet.viewsets.vehicle_info_viewsets import VehicleInfoViewSet
from fleet.viewsets.vehicle_booking_viewserts import VehicleBookingViewSet
from fleet.viewsets.type_info_viewsets import (
    FuelTypeViewSet, VehicleTypeViewSet, DepartmentViewSet,
    UserRoleInfoViewSet, LicenseClassInfoViewSet
)

router = routers.SimpleRouter()
router.register(r'staffs', UserProfileViewSet, basename='staffs')
router.register(r'user-info', UserInfoViewSet, basename='user_info')
router.register(r'service-form', ServiceFormViewSet, basename='service_form')
router.register(r'workshop-info', WorkshopInfoViewSet, basename='workshop_info')
router.register(r'job-code', JobIDInfoViewSet, basename='job_code')
router.register(r'infringement', InfringementViewSets, basename='infringement')
router.register(r'vehicle-info', VehicleInfoViewSet, basename='vehicle_info')
router.register(r'vehicle-booking', VehicleBookingViewSet, basename='vehicle_booking')
router.register(r'fuel-type', FuelTypeViewSet, basename='fuel_type')
router.register(r'vehicle-type', VehicleTypeViewSet, basename='vehicle_type')
router.register(r'pool', DepartmentViewSet, basename='department_type')
router.register(r'role', UserRoleInfoViewSet, basename='role')
router.register(r'license-class', LicenseClassInfoViewSet, basename='license_class')
