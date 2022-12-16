
from rest_framework.views import APIView
from apps.custom_response import CustomResponse
from .serializers import CategorySerializer, CategoryDetailSerializer
from .models import Category

class DetailCategoryView(APIView):
    def get(self, request, slug):
        try:
            category_item = Category.objects.get(slug = slug)
            serializer = CategoryDetailSerializer(category_item)
            return CustomResponse.success(serializer.data)

        except Category.DoesNotExist:
            return CustomResponse.notFound(error='Category Not Found')

class CategoryView(APIView):
    def get(self, request):
        try:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return CustomResponse.success(serializer.data)

        except Category.DoesNotExist:
            return CustomResponse.notFound(error='Category Not Found')