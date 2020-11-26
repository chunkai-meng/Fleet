from rest_framework import permissions
from fleet.models import UserInfo


class IsFleetUser(permissions.BasePermission):
    message = "You're not a Fleet user, please create new User in UserInfo."

    def has_permission(self, request, view):
        return bool(UserInfo.objects.filter(SAMAccountName=request.user.sam_account_name).exists())
