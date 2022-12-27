from django.db import models
from product.models import Product

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
    total = models.PositiveIntegerField()

    shiftPengantaran = models.CharField(max_length=32)
    pembayaran = models.CharField(max_length=32)
    status = models.CharField(max_length=32, default="Belum Dibayar")

    def __str__(self):
        return self.namaPembeli

class TransactionProduct(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_slug = models.CharField(max_length=32)
    quantity = models.PositiveIntegerField(default=1)