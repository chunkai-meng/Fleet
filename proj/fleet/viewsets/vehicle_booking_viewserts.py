from rest_framework import mixins, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from api_base import viewsets
from ..base_viewsets import BaseViewSetMixin
from ..models import VehicleBooking, UserInfo, VehicleInfo, BookingStatusIDInfo
from ..serializers.vehicle_booking_serializers import VehicleBookingSerializer


class VehicleBookingViewSet(BaseViewSetMixin,
                            mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin, mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """
    Status:
    0	PendingBooking
    1	Approved
    2	Rejected
    3	Did not use
    4	Returned
    5	PendingReturn

    my_bookings:
    - **All my bookings:** /api/vehicle-booking/my-bookings/
    - **My specific booking:** /api/vehicle-booking/my-bookings/?SN=VB210111020804
    """

    queryset = VehicleBooking.objects.all()
    serializer_class = VehicleBookingSerializer
    lookup_field = 'SN'

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

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
    def return_vehicle(self, request, SN):
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

    @action(detail=False, methods=['get'], url_path='pending-list')
    def pending_list(self, request):
        """
        = Sandy's /API/VehicleBooking/TotalList/Pending
        """
        queryset = self.get_queryset().filter(Status__in=[0, 5])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='approve-booking')
    def approve_booking(self, request, SN):
        """
        = Sandy's /API/VehicleBooking/PendingApprove/Submitted
        """
        obj = self.get_object()
        # print('booking status:', obj.Status.StatusID)
        if obj.Status.StatusID == 0:
            obj.__dict__.update(request.data)
            obj.Status = BookingStatusIDInfo.objects.get(StatusName='Approved')
            obj.save()

            # update vehicle
            vehicle = VehicleInfo.objects.get_or_none(VehicleID=obj.VehicleID)
            vehicle.Status = 0
            vehicle.save()

            serializer = self.get_serializer(obj, many=False)
            return Response(serializer.data)
        else:
            raise serializers.ValidationError('This booking is not pending approval.')

    @action(detail=True, methods=['get'], url_path='reject-booking')
    def reject_booking(self, request, SN):
        """
        = Sandy's /API/VehicleBooking/PendingApprove/Reject
        """
        obj = self.get_object()
        # print('Booking Status', obj.Status.StatusID)
        if obj.Status.StatusID == 0:
            obj.Status = BookingStatusIDInfo.objects.get(StatusName='Rejected')
            obj.save()
            serializer = self.get_serializer(obj, many=False)
            return Response(serializer.data)
        else:
            raise serializers.ValidationError("This booking is not pending approval.")

    @action(detail=True, methods=['get'], url_path='approve-return')
    def approve_return(self, request, SN):
        """
        = Sandy's /API/VehicleBooking/PendingReturn/Edit
        """
        obj = self.get_object()
        if obj.Status == 5:
            obj.__dict__.update(request.data)
            obj.Status = 4
            obj.save()

            # update vehicle
            vehicle = VehicleInfo.objects.get_or_none(VehicleID=obj.VehicleID)
            vehicle.Status = 1
            vehicle.save()

            serializer = self.get_serializer(obj, many=False)
            return Response(serializer.data)
        else:
            raise serializers.ValidationError('This booking is not pending return.')
