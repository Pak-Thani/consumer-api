from django.db import models
from image_optimizer.fields import OptimizedImageField

import uuid
import pathlib

def imageUploadHandler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    return f"category/{new_fname}{fpath.suffix}"

class Category(models.Model):
  name = models.CharField(max_length=32)
  image = OptimizedImageField( 
    upload_to=imageUploadHandler,
    optimized_image_output_size=(400, 300),
    optimized_image_resize_method="thumbnail"
  )
  slug = models.CharField(max_length=32)

  def __str__(self):
        return self.name
