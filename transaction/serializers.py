from rest_framework import serializers
from product.serializers import ProductSerializer
from .models import Transaction
class TransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    # quantity = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Transaction
        fields = ('id', 'created', 'namaPembeli', 'nomorWhatsapp', 'kabupaten', 'kecamatan', 'detailAlamat', 'alamat', 'product', 'quantity', 'total', 'pembayaran', 'status')
