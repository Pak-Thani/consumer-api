from django.shortcuts import render
from apps.custom_response import CustomResponse
from .serializers import TransactionSerializer
from rest_framework.views import APIView

class TransactionView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse.success(serializer.data)

        return CustomResponse.badRequest(serializer.errors)