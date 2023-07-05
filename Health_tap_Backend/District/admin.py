from django.contrib import admin
from District.models import District


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en', 'city')
    list_filter = ('city',)
    search_fields = ('name_ar', 'name_en', 'city__name_ar', 'city__name_en')
    ordering = ('city__name_en', 'name_en')
    fieldsets = (
        (None, {
            'fields': ('name_ar', 'name_en', 'city')
        }),
    )


admin.site.register(District, DistrictAdmin)
