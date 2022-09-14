from rest_framework import serializers
from .models import CustomSection

class CustomSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomSection
        fields = ['id', 'title', 'slug', 'products']
        extra_kwargs = {'products': {'required': False}}
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }