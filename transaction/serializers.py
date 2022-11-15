from rest_framework import serializers
from product.serializers import ProductSerializer
from .models import Transaction, TransactionProduct
from drf_writable_nested import WritableNestedModelSerializer

class TransactionProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = TransactionProduct
        fields = ('id', 'product', 'transaction', 'quantity')
        
class TransactionSerializer(WritableNestedModelSerializer):
    products = TransactionProductSerializer(many=True)
    class Meta:
        model = Transaction
        fields = ('id', 'created', 'namaPembeli', 'nomorWhatsapp', 'kabupaten', 'kecamatan', 'detailAlamat', 'alamat', 'products', 'total', 'pembayaran', 'status')

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        transaction = Transaction.objects.create(**validated_data)
        for product_data in products_data:
            TransactionProduct.objects.create(transaction=transaction, **product_data)
        return transaction