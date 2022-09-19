from django.contrib import admin

from .models import CustomSection

class CustomSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active')

admin.site.register(CustomSection, CustomSectionAdmin)
