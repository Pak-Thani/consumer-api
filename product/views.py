from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer
from apps.custom_response import CustomResponse

class ProductView(APIView):
    def get(self, request, slug):
        try:
            product_item = Product.objects.get(slug = slug)
            serializer = ProductSerializer(product_item)
            return CustomResponse.success(serializer.data)
        except Exception as e:
            return CustomResponse.notFound(error=e)
