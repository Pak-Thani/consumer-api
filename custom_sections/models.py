from django.db import models
from product.models import Product
from django.utils.text import slugify

class CustomSection(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    is_active = models.BooleanField(default=False)
    products = models.ManyToManyField(Product, blank=True)

    def onlyGetSixProducts(self):
        return Product.objects.all()[:6]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(CustomSection, self).save(*args, **kwargs)