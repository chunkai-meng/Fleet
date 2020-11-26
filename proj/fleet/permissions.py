from rest_framework import permissions
from fleet.models import UserInfo


class IsFleetUser(permissions.BasePermission):
    message = "You're not a Fleet user, please create new User in UserInfo."

    def has_permission(self, request, view):
        print(request.user.sam_account_name)
        return UserInfo.objects.filter(SAMAccountName=request.user.sam_account_name).exists()

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
