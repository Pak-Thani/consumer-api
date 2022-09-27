from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('name', 'slug', 'qty', 'pricePerQty', 'stockAvailable', 'isStockAvailable', 'image')
=======
    list_display = ('name', 'slug', 'qty', 'pricePerQty', 'stockAvailable', 'isStockAvailable')
>>>>>>> 17f8a336d23d38e9162c325e557de9bbf57ade23
    readonly_fields = ('isStockAvailable', )

    def save_model(self, request, obj, form, change):
        if obj.stockAvailable > 0:
            obj.isStockAvailable = True
        else:
            obj.isStockAvailable = False
        obj.save()

    

admin.site.register(Product, ProductAdmin)