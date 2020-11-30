from rest_framework import permissions
from fleet.models import UserInfo
from . import enums


class IsFleetUser(permissions.BasePermission):
    message = "You're not a Fleet user, please create new User in UserInfo."

    def has_permission(self, request, view):
        print(request.user.is_authenticated)
        return bool(request.user.is_authenticated and UserInfo.objects.filter(
            SAMAccountName=request.user.sam_account_name).exists())


class IsAdminUser(permissions.BasePermission):
    message = "You're not a Fleet Admin, please developer."

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            current_user_info = UserInfo.objects.get_or_none(SAMAccountName=request.user.sam_account_name)
            return bool(current_user_info and current_user_info.Role == enums.ROLE_ADMIN)
        else:
            return False
