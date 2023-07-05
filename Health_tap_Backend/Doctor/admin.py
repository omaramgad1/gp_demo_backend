from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Doctor
# Register your models here.


class DoctorAdmin(UserAdmin):
    # The fields to be used in displaying the Doctor model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'id', 'first_name', 'last_name', 'profLicenseNo',
                    'specialization', 'city', 'district', 'is_active')
    list_filter = ('specialization', 'city', 'district',
                   'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',
         'profLicenseNo', 'specialization', 'city', 'district', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    # add_fieldsets is not a standard UserAdmin attribute. DoctorAdmin
    # overrides get_fieldsets to use this attribute when creating a doctor.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'profLicenseNo', 'specialization', 'city', 'district', 'address', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name', 'profLicenseNo')
    ordering = ('email', 'id')
    filter_horizontal = ()


admin.site.register(Doctor, DoctorAdmin)
