from rest_framework import serializers
from product.serializers import ProductSerializer
from .models import Transaction, TransactionProduct
class TransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    

    class Meta:
        model = Transaction
        fields = ('id', 'created', 'namaPembeli', 'nomorWhatsapp', 'kabupaten', 'kecamatan', 'detailAlamat', 'alamat', 'products', 'total', 'pembayaran', 'status')

class TransactionProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionProduct
        fields = ('id', 'product', 'quantity')