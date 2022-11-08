from rest_framework import serializers
from product.serializers import ProductSerializer
from .models import Transaction, TransactionProduct

class TransactionProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = TransactionProduct
        fields = ('id', 'product', 'quantity')
        
class TransactionSerializer(serializers.ModelSerializer):
   products = TransactionProductSerializer(many=True, read_only=True)
   class Meta:
        model = Transaction
        fields = ('id', 'created', 'namaPembeli', 'nomorWhatsapp', 'kabupaten', 'kecamatan', 'detailAlamat', 'alamat', 'products', 'total', 'pembayaran', 'status')