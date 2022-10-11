from email.policy import default
from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='banner/')