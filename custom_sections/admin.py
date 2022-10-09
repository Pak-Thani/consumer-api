from django.contrib import admin

from .models import CustomSection

class CustomSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active')
    readonly_fields = ('slug',)

admin.site.register(CustomSection, CustomSectionAdmin)
