from email.policy import default
from django.db import models
import uuid
import pathlib

from image_optimizer.fields import OptimizedImageField

def imageUploadHandler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    return f"banner/{new_fname}{fpath.suffix}"

class Banner(models.Model):
    name = models.CharField(max_length=32)
    image = OptimizedImageField(
        upload_to=imageUploadHandler,
        optimized_image_output_size=(400, 300),
        optimized_image_resize_method="thumbnail"
    )