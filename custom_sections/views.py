
from rest_framework.views import APIView
from apps.custom_response import CustomResponse
from .serializer import CustomSectionSerializer, CustomSectionDetailSerializer
from .models import CustomSection

# Create your views here.
class CustomSectionView(APIView):
    def get(self, request, slug=None):
        if slug is None:
            custom_sections = CustomSection.objects.all()
            serializer = CustomSectionSerializer(custom_sections, many=True)
            return CustomResponse.success(serializer.data)
        else:
            try:
                custom_section = CustomSection.objects.get(slug=slug)
                serializer = CustomSectionDetailSerializer(custom_section)
                return CustomResponse.success(serializer.data)
            except CustomSection.DoesNotExist:
                return CustomResponse.notFound()
    
    # def post(self, request):
    #     serializer = CustomSectionDetailSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return CustomResponse.success(serializer.data)
    #     else:
    #         return CustomResponse.badRequest(serializer.errors)

    # def put(self, request, slug):
    #     try:
    #         custom_section = CustomSection.objects.get(slug=slug)
    #         serializer = CustomSectionDetailSerializer(custom_section, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return CustomResponse.success(serializer.data)
    #         else:
    #             return CustomResponse.badRequest(serializer.errors)
    #     except CustomSection.DoesNotExist:
    #         return CustomResponse.notFound()

    # def delete(self, request, slug):
    #     try:
    #         custom_section = CustomSection.objects.get(slug=slug)
    #         custom_section.delete()
    #         return CustomResponse.success()
    #     except CustomSection.DoesNotExist:
    #         return CustomResponse.notFound()
