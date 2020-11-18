from rest_framework import permissions
from rest_framework.serializers import ValidationError
from django.conf import settings


class IsOwner(permissions.BasePermission):
    message = "Own Only"

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, 'owner'):
            return obj.owner == request.user or request.user.is_superuser
        else:
            return obj.created_by == request.user or request.user.is_superuser


class IsCheckoutTeam(permissions.BasePermission):
    message = "only groups 'ACCOUNTING_GROUP' 'INVENTORY_MANAGER_GROUP' 'CHECKOUT_GROUP' can edit"

    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.values_list('name', flat=True)
        return bool(settings.GROUP_NAME['ACCOUNTING_GROUP'] in user_groups or
                    settings.GROUP_NAME['INVENTORY_MANAGER_GROUP'] in user_groups or
                    settings.GROUP_NAME['CHECKOUT_GROUP'] in user_groups)


class IsAccounting(permissions.BasePermission):
    message = "only groups 'ACCOUNTING_GROUP' access Procurement data"

    def has_permission(self, request, view):
        return is_account_team(request.user)

    def has_object_permission(self, request, view, obj):
        return is_account_team(request.user)


def is_audit_team(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return bool(settings.GROUP_NAME['AUDIT_GROUP'] in user_groups)


def is_account_team(user):
    user_groups = user.groups.values_list('name', flat=True)
    return bool(settings.GROUP_NAME['ACCOUNTING_GROUP'] in user_groups)
