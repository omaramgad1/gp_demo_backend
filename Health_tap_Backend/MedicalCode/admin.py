from django.contrib import admin
from MedicalCode.models import MedicalEditCode


class MedicalEditCodeAdmin(admin.ModelAdmin):
    list_display = ('patient', 'code', 'appointment',
                    'status', 'created_at', 'expired_at')
    list_filter = ('status',)
    search_fields = ('patient__name',)
    ordering = ('-created_at',)
    readonly_fields = ('code', 'created_at', 'expired_at')


admin.site.register(MedicalEditCode, MedicalEditCodeAdmin)
