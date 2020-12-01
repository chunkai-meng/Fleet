from rest_framework import mixins
from api_base import viewsets
from ..base_viewsets import BaseViewSetMixin
from ..models import VehicleBooking
from ..serializers.vehicle_booking_serializers import VehicleBookingSerializer


class VehicleBookingViewSet(BaseViewSetMixin,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = VehicleBooking.objects.all()
    serializer_class = VehicleBookingSerializer
