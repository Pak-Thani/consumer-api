from email.policy import default
from django.db import models

class Product(models.Model):
    name =  models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    image = models.FileField(upload_to='product/')
    slug = models.CharField(max_length=8)
    qty = models.CharField(max_length=8)
    pricePerQty = models.PositiveIntegerField()
    stockAvailable = models.PositiveIntegerField()
    isStockAvailable = models.BooleanField()
    
