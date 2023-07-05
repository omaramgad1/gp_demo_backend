from django.contrib import admin
from .models import Patient
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class PatientAdmin(UserAdmin):
    # The fields to be used in displaying the Patient model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'phone', 'national_id',
                    'is_patient', 'is_active')
    list_filter = ('gender',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',
         'date_of_birth', 'phone', 'gender', 'national_id',)}),
        ('Permissions', {'fields': ('is_patient',
         'is_staff', 'is_active', 'is_superuser')}),
    )
    # add_fieldsets is not a standard UserAdmin attribute. PatientAdmin
    # overrides get_fieldsets to use this attribute when creating a patient.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'gender', 'date_of_birth', 'phone', 'national_id', 'profileImgUrl', 'email', 'password1', 'password2',  'is_active'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'id')
    filter_horizontal = ()


# Register the PatientAdmin class with the admin site
admin.site.register(Patient, PatientAdmin)
