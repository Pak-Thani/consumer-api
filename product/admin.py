from django.contrib import admin
from import_export.admin import ImportMixin
from .resources import ProductResource
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'qty', 'pricePerQty', 'stockAvailable', 'isStockAvailable', 'image')
    readonly_fields = ('isStockAvailable', )
    resource_class = ProductResource

    def save_model(self, request, obj, form, change):
        if obj.stockAvailable > 0:
            obj.isStockAvailable = True
        else:
            obj.isStockAvailable = False
        obj.save()

    

admin.site.register(Product, ProductAdmin)