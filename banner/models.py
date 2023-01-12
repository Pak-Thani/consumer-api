from email.policy import default
from django.db import models

from image_optimizer.fields import OptimizedImageField

class Banner(models.Model):
    name = models.CharField(max_length=32)
    image = OptimizedImageField(
        upload_to='banner/',
        optimized_image_resize_method="thumbnail"
    )