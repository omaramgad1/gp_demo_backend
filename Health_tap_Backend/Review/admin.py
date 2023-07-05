from django.contrib import admin
from .models import Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'rate', 'comment')
    list_filter = ('rate',)
    search_fields = ('patient__name', 'doctor__name')
    ordering = ('-id',)
    readonly_fields = ('patient', 'doctor', 'rate', 'comment')


admin.site.register(Review, ReviewAdmin)
