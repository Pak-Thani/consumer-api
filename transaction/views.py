from django.shortcuts import render
from apps.custom_response import CustomResponse
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.views import APIView

class TransactionView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse.success(serializer.data)

        return CustomResponse.badRequest(serializer.errors)

    # def put(self, request, id):
        # try:
        #     transaction = Transaction.objects.get(id=id)
        #     serializer = TransactionSerializer(transaction, data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return CustomResponse.success(serializer.data)

        #     return CustomResponse.error(serializer.errors, 400)

        # except Transaction.DoesNotExist:
        #     return CustomResponse.notFound(error='Transaction not found')