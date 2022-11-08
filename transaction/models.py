from django.db import models
from product.models import Product
from django.contrib.postgres.fields import ArrayField

class Transaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    #customer data
    namaPembeli = models.CharField(max_length=32)
    nomorWhatsapp = models.CharField(max_length=16)

    #address
    kabupaten = models.CharField(max_length=32)
    kecamatan = models.CharField(max_length=32)
    detailAlamat = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)

    #cart
    products = models.ManyToManyField(Product, through='TransactionProduct')
    total = models.IntegerField()

    pembayaran = models.CharField(max_length=32)
    status = models.CharField(max_length=32, default="Belum Dibayar")

    def __str__(self):
        return self.namaPembeli

class TransactionProduct:
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField()