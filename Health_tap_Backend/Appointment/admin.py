from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'start_time',
                    'duration', 'price', 'status')
    list_filter = ('doctor', 'status')
    search_fields = ('doctor__name',)
    ordering = ('-date', 'start_time')
    fieldsets = (
        (None, {
            'fields': ('doctor', 'date', 'start_time', 'duration', 'price')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )


admin.site.register(Appointment, AppointmentAdmin)
