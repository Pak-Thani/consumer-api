from django.db import models

class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=32)
    kabupaten = models.CharField(max_length=32)
    kecamatan = models.CharField(max_length=32)
    addressDetail = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    whatsappNumber = models.CharField(max_length=16)
    payment = models.CharField(max_length=32)
    status = models.CharField(max_length=32)

    def __str__(self):
        return self.name
