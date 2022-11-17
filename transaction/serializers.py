from rest_framework import serializers
from .models import Transaction, TransactionProduct, Product
from product.serializers import ProductSerializer



class TransactionProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='product.id')
    product = serializers.ReadOnlyField(source='product.name')
    class Meta:
        model = TransactionProduct
        fields = ('id', 'product', 'product_slug', 'quantity')

class TransactionSerializer(serializers.ModelSerializer):
    products = TransactionProductSerializer(source="transactionproduct_set", many=True)
    class Meta:
        model = Transaction
        fields = '__all__'
        depth = 2

    def create(self, validated_data):
        products_data = validated_data.pop('transactionproduct_set')
        transaction = Transaction.objects.create(**validated_data)
        for product_data in products_data:
            print(product_data)
            TransactionProduct.objects.create(
                transaction=transaction, 
                product=Product.objects.get(slug=product_data['product_slug']),
                product_slug=product_data['product_slug'],
                quantity=product_data['quantity']
            )
        return transaction