
from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=32)
  icon = models.CharField(max_length=255)
  slug = models.CharField(max_length=32)

  def __str__(self):
        return self.name
