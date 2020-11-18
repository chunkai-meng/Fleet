from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    # actions = ['soft_delete']
    # exclude = ('is_deleted',)
    list_per_page = 15

    # def soft_delete(self, request, queryset):
    #     queryset.update(is_deleted=True)
    #
    # soft_delete.short_description = "Soft Delete Selected Items"

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.is_superuser and request.user.username == 'admin':
            return actions
        else:
            if 'delete_selected' in actions:
                del actions['delete_selected']

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        if isinstance(list_display, list):
            return list_display + ['deleted']
        else:
            return list_display + ('deleted',)

    # def get_readonly_fields(self, request, obj=None):
    #     read_only = super().get_readonly_fields(request, obj)
    #     if isinstance(read_only, list):
    #         return read_only + ['deleted']
    #
    #     else:
    #         return read_only + ('delete',)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser and obj and not obj.deleted

    # def get_list_display(self, request):
    #     list_display = super().get_list_display(request)
    #     if request.user.is_superuser:
    #         return list_display + ('is_deleted',)
    #     return list_display

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(is_deleted=False)

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = request.user
        instance.updated_by = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        if len(instances) and hasattr(instances[0], 'created_by'):
            for instance in instances:
                if not change or not instance.created_by:
                    instance.created_by = request.user
                instance.updated_by = request.user
                instance.save()

        formset.save_m2m()


class BaseInline(admin.TabularInline):
    exclude = ('updated_by',)
    extra = 0
    # max_num = 5
    can_delete = True

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.all_valid()
    #
    # def get_exclude(self, request, obj=None):
    #     if request.user.is_superuser and request.user.username == 'admin':
    #         return self.exclude
    #     elif self.exclude is None:
    #         return ['is_deleted']
    #     else:
    #         return self.exclude + ('is_deleted',)

    # class Media:
    #     css = {
    #         "all": ('inventory/css/admin/hide_admin_original.css',)
    #     }
