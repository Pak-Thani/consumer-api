from rest_framework import serializers
from product.serializers import ProductSerializer
from .models import CustomSection

class CustomSectionSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True, source='onlyGetSixProductsBySlug')
    class Meta:
        model = CustomSection
        fields = ['id', 'title', 'slug', 'products', 'is_active']
        extra_kwargs = {
            'products': {
                'required': False, 
                'read_only': True,
            }
        }
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class CustomSectionDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomSection
        fields = ['id', 'title', 'slug', 'products', 'is_active']
        extra_kwargs = {'products': {'required': False, 'read_only': True}}
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }