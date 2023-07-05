from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'appointment', 'status')
    list_filter = ('status',)
    search_fields = ('patient__name', 'appointment__doctor__name')
    ordering = ('-appointment__date', 'appointment__start_time')
    readonly_fields = ('status',)


admin.site.register(Reservation, ReservationAdmin)
