from django.db import models

class Product(models.Model):
    name =  models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    slug = models.CharField(max_length=30)

    
