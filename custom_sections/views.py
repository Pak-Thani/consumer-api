from rest_framework import viewsets
from .serialize import CustomSectionSerializer
from .models import CustomSection

# Create your views here.
class CustomSectionView(viewsets.ModelViewSet):
    queryset = CustomSection.objects.all()
    serializer_class = CustomSectionSerializer
    lookup_field = 'slug'
