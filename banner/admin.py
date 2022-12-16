from django.contrib import admin

from .models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'image')

    def save_model(self, request, obj, form, change):
        obj.save()

    

admin.site.register(Banner, BannerAdmin)