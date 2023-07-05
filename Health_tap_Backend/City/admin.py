from django.contrib import admin
from City.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en')
    search_fields = ('name_ar', 'name_en')
    ordering = ('name_en',)


admin.site.register(City, CityAdmin)
