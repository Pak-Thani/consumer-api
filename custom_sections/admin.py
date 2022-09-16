from django.contrib import admin

# Register your models here.
from .models import CustomSection

class CustomSectionAdmin(admin.ModelAdmin):
    # display title, slug, is_active, and products
    list_display = ('title', 'slug', 'is_active')

admin.site.register(CustomSection, CustomSectionAdmin)
