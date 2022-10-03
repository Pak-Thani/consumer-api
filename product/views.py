from rest_framework.views import APIView
from rest_framework import generics
from product.models import Product
from product.serializers import ProductSerializer
from product.paginations import CustomPagination
from apps.custom_response import CustomResponse

class ProductView(APIView):
    def get(self, request, slug):
        try:
            product_item = Product.objects.get(slug = slug)
            serializer = ProductSerializer(product_item)
            return CustomResponse.success(serializer.data)

        except Product.DoesNotExist:
            return CustomResponse.notFound(error='Product Not Found')

class SearchProductView(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = ProductSerializer

    def get(self, request, keyword):
        try:
            products = Product.objects.filter(name__icontains = keyword)
            serializer = self.serializer_class(products, many=True)

            page = self.paginate_queryset(products)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                data = self.get_paginated_response(serializer.data)
                return CustomResponse.success(data)
                
        except Product.DoesNotExist:
            return CustomResponse.notFound(error='Product Not Found')
