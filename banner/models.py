from email.policy import default
from django.db import models
from image_optimizer.fields import OptimizedImageField

class Banner(models.Model):
    name = models.CharField(max_length=32)
    # image = models.ImageField(upload_to='banner/')
    image = OptimizedImageField(
        upload_to='banner/',
        optimized_image_output_size=(400, 300),
        optimized_image_resize_method="thumbnail"
    )