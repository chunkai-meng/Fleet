from django.contrib import admin
from .base_admin import BaseAdmin
from django.db import models
from django.forms import Textarea


class CommonCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class CommonInfoAdmin(BaseAdmin):
    list_per_page = 20
    date_hierarchy = 'updated_at'
    ordering = ('-updated_at',)

    raw_id_fields = ['owner']
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 80})},
    }

    def get_changeform_initial_data(self, request):
        get_data = super(
            CommonInfoAdmin, self).get_changeform_initial_data(request)
        return get_data or {
            'owner': request.user.pk
        }

    def get_readonly_fields(self, request, obj):
        if request.user.is_superuser and request.user.username == 'admin':
            return self.readonly_fields
        else:
            return self.readonly_fields + ('is_deleted')
