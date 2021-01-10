from rest_framework import mixins, serializers
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
    """
    my_bookings:
    - **All my bookings:** /api/vehicle-booking/my-bookings/
    - **My specific booking:** /api/vehicle-booking/my-bookings/?SN=VB210111020804
    """
    queryset = VehicleBooking.objects.all()
    serializer_class = VehicleBookingSerializer
    lookup_field = 'SN'

    @action(detail=False, methods=['get'], url_path='my-bookings')
    def my_bookings(self, request):
        sn = request.query_params.get('SN', None)
        current_user = self.get_current_user(request)
        queryset = self.get_queryset().filter(UserID=current_user.UserID.hex)
        if sn:
            queryset = queryset.filter(SN=sn)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='return')
    def return_booking(self, request, SN):
        obj = self.get_object()
        if obj.Status != 1:
            msg = 'Only Approved(Status=1) booking can be returned'

        if obj.StartedMileage and float(obj.StartedMileage) <= float(request.data.get('ReturnedMileage', 0)):
            obj.__dict__.update(request.data)
            obj.Status = 5
            obj.save()
            serializer = self.get_serializer(obj, many=False)
            return Response(serializer.data)
        else:
            msg = 'ReturnedMileage cannot be smaller than StartedMileage'

        raise serializers.ValidationError(msg)
