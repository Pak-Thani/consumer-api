
from rest_framework.views import APIView
from apps.custom_response import CustomResponse
from .serializer import CustomSectionSerializer, CustomSectionDetailSerializer
from .models import CustomSection
from .paginations import CustomPagination
from rest_framework import generics


class DetailCustomSectionView(generics.RetrieveAPIView):
    serializer_class = CustomSectionDetailSerializer
    lookup_field = 'slug'

    def get(self, request, slug):
        try:
            custom_section = CustomSection.objects.get(slug=slug)
            serializer = self.serializer_class(custom_section)
            return CustomResponse.success(serializer.data)
        except CustomSection.DoesNotExist:
            return CustomResponse.error('Custom section not found', 404)

class ListCustomSectionView(generics.ListAPIView):
    queryset = CustomSection.objects.all().filter(is_active=True)
    pagination_class = CustomPagination
    serializer_class = CustomSectionSerializer

    def get(self, request):
        try:
            custom_section = self.get_queryset()
            serializer = self.serializer_class(custom_section, many=True)

            page = self.paginate_queryset(custom_section)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                data = self.get_paginated_response(serializer.data)
                return CustomResponse.success(data)
        except CustomSection.DoesNotExist:
            return CustomResponse.error('Custom section not found', 404)

# Create your views here.
# class CustomSectionView(APIView):
#     pagination_class = CustomPagination

#     def get(self, request, slug=None):
#         if slug is None:
#             custom_sections = CustomSection.objects.all()
#             serializer = CustomSectionSerializer(custom_sections, many=True)
#             return CustomResponse.success(serializer.data)
#         else:
#             try:
#                 custom_section = CustomSection.objects.get(slug=slug)
#                 serializer = CustomSectionDetailSerializer(custom_section)
#                 return CustomResponse.success(serializer.data)
#             except CustomSection.DoesNotExist:
#                 return CustomResponse.notFound()
