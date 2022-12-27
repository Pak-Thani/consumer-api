from django.db import models
from category.models import Category
from image_optimizer.fields import OptimizedImageField
from django.utils.text import slugify

import uuid
import pathlib

def imageUploadHandler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    return f"product/{new_fname}{fpath.suffix}"

class Product(models.Model):
    name =  models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    image = OptimizedImageField(
        upload_to=imageUploadHandler,
        optimized_image_output_size=(400, 300),
        optimized_image_resize_method="thumbnail"
    )
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    qty = models.CharField(max_length=32)
    pricePerQty = models.PositiveIntegerField()
    stockAvailable = models.PositiveIntegerField(default=0)
    isStockAvailable = models.BooleanField()
    category = models.ForeignKey(Category, related_name='products', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

