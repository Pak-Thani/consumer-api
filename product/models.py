from email.policy import default
from django.db import models

class Product(models.Model):
    name =  models.CharField(max_length=32)
    description = models.CharField(max_length=255)
<<<<<<< HEAD
    image = models.FileField(upload_to="products/")
=======
    image = models.CharField(max_length=255)
>>>>>>> 17f8a336d23d38e9162c325e557de9bbf57ade23
    slug = models.CharField(max_length=8)
    qty = models.CharField(max_length=8)
    pricePerQty = models.PositiveIntegerField()
    stockAvailable = models.PositiveIntegerField()
    isStockAvailable = models.BooleanField()
    
