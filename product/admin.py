from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'qty', 'pricePerQty', 'stockAvailable', 'isStockAvailable')
    readonly_fields = ('isStockAvailable', )

    def save_model(self, request, obj, form, change):
        if obj.stockAvailable > 0:
            obj.isStockAvailable = True
        else:
            obj.isStockAvailable = False
        obj.save()

    

admin.site.register(Product, ProductAdmin)