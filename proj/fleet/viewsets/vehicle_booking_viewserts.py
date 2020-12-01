from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from api_base import viewsets
from ..base_viewsets import BaseViewSetMixin
from ..models import VehicleBooking, UserInfo
from ..serializers.vehicle_booking_serializers import VehicleBookingSerializer


class VehicleBookingViewSet(BaseViewSetMixin,
                            mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = VehicleBooking.objects.all()
    serializer_class = VehicleBookingSerializer
    lookup_field = 'SN'

    @action(detail=False, methods=['get'], url_path='my_bookings')
    def my_bookings(self, request):
        current_user = self.get_current_user(request)
        queryset = self.get_queryset().filter(UserID=current_user.UserID.hex)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
