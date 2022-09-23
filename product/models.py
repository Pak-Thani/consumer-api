from django.db import models
from category.models import Category

class Product(models.Model):
    name =  models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    slug = models.CharField(max_length=32)
    qty = models.CharField(max_length=32)
    pricePerQty = models.PositiveIntegerField()
    stockAvailable = models.PositiveIntegerField()
    isStockAvailable = models.BooleanField()
    category = models.ForeignKey(Category, related_name='products', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

