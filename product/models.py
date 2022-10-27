from django.db import models
from category.models import Category
from image_optimizer.fields import OptimizedImageField

class Product(models.Model):
    name =  models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    #image = models.FileField(upload_to='product/')
    image = OptimizedImageField(
        upload_to='banner/',
        optimized_image_output_size=(400, 300),
        optimized_image_resize_method="thumbnail"
    )
    slug = models.CharField(max_length=32)
    qty = models.CharField(max_length=32)
    pricePerQty = models.PositiveIntegerField()
    stockAvailable = models.PositiveIntegerField()
    isStockAvailable = models.BooleanField()
    category = models.ForeignKey(Category, related_name='products', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

