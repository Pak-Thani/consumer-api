
from django.db import models
from image_optimizer.fields import OptimizedImageField
from django.utils.text import slugify

class Category(models.Model):
  name = models.CharField(max_length=32)
  image = OptimizedImageField( 
    upload_to='icon-category/',
    optimized_image_resize_method="thumbnail"
  )
  slug = models.SlugField(max_length=100, unique=True, editable=False)

  def __str__(self):
        return self.name

  def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
