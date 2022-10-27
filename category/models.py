
from django.db import models
from image_optimizer.fields import OptimizedImageField

class Category(models.Model):
  name = models.CharField(max_length=32)
  #icon = models.FileField(upload_to='icon-category/')
  image = OptimizedImageField( 
    upload_to='banner/',
    optimized_image_output_size=(400, 300),
    optimized_image_resize_method="thumbnail"
  )
  slug = models.CharField(max_length=32)

  def __str__(self):
        return self.name
