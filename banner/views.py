from rest_framework.views import APIView

from banner.models import Banner
from banner.serializers import BannerSerializer
from apps.custom_response import CustomResponse
from django.http import JsonResponse
import json
from rest_framework import generics
from apps.custom_response import CustomResponse


class BannerView(APIView):
    def get(self, request, slug):
        try:
            bannert_item = Banner.objects.get(slug = slug)
            serializer = BannerSerializer(bannert_item)
            return CustomResponse.success(serializer.data)

        except Banner.DoesNotExist:
            return CustomResponse.notFound(error='Banner Not Found')
    


class JsonView(generics.ListAPIView):

    def get(self, request):
        try:
            data = Banner.objects.all()
            seriliazer = BannerSerializer(data, many=True)
            return CustomResponse.success(seriliazer.data)

        except Banner.DoesNotExist:
            return CustomResponse.notFound(error='Json Not Found')

