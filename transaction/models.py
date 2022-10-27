from django.db import models

class Transaction(models.Model):
    nama = models.CharField(max_length=32)
    kabupaten = models.CharField(max_length=32)
    kecamatan = models.CharField(max_length=32)
    alamat_detail = models.CharField(max_length=32)
    alamat = models.CharField(max_length=32)
    nomor_telepon = models.CharField(max_length=16)
    pembayaran = models.CharField(max_length=32)

    def __str__(self):
        return self.nama
