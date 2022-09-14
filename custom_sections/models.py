from django.db import models
from product.models import Product

# Create your models here.
class CustomSection(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, blank=True)

    def onlyGetSixProducts(self):
        return Product.objects.all()[:6]

    