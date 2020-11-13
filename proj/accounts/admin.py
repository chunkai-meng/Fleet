from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import UserProfile
from .forms import GroupAdminForm
from simple_history.admin import SimpleHistoryAdmin


class UserProfileAdmin(UserAdmin, SimpleHistoryAdmin):
    list_display = (
        'id',
        'username', 'email', 'first_name',
        'last_name', 'last_login', 'date_joined',
        'is_staff', 'is_active'
    )
    list_display_links = ['username']
    fieldsets = (
        ('LDAP Fields', {'fields': ('cn_name', 'display_name')}),
        ('Django ID', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_editable = ['is_staff']
    list_per_page = 30
    ordering = ['id']


# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'members')
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']
    ordering = ('id',)

    def members(self, obj):
        if obj:
            return ', '.join(obj.user_set.order_by('username').values_list('username', flat=True))
        else:
            return ''


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
