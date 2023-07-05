from django.contrib import admin
from .models import MedicalEntry
# Register your models here.


class MedicalEntryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment',
                    'created_at', 'updated_at')
    list_filter = ('patient', 'doctor', 'appointment__date')
    search_fields = ('patient__name', 'doctor__name')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('patient', 'doctor', 'appointment', 'comment', 'prescription', 'analysis_image')
        }),
    )


admin.site.register(MedicalEntry, MedicalEntryAdmin)
