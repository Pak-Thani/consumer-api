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

    def get(self, request, id):
        try:
            transaction = Transaction.objects.get(id = id)
            serializer = TransactionSerializer(transaction)
            return CustomResponse.success(serializer.data)

        except Transaction.DoesNotExist:
            return CustomResponse.notFound(error='Transaction Not Found')

    def put(self, request, id):
        try:
            transaction = Transaction.objects.get(id = id)
            transaction.buktiPembayaran = request.data['buktiPembayaran']
            transaction.save()    

            serializer = TransactionSerializer(transaction)
            return CustomResponse.success(serializer.data)

        except Transaction.DoesNotExist:
            return CustomResponse.notFound(error='Transaction Not Found')