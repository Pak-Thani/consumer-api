from django.http import JsonResponse

class CustomResponse:

    def base(self, values=None, error="", isSuccess=True, status=200):
        if values is None:
            values = []

        return JsonResponse({
            'success': isSuccess,
            'error': error,
            'data': values,
        }, status=status)
    
    @staticmethod
    def success(values=None, error=""):
        return CustomResponse().base(values=values, error=error, isSuccess=True, status=200)

    @staticmethod
    def unauthorized(values=None, error="Unauthroized access"):
        return CustomResponse().base(values=values, error=error, isSuccess=False, status=401)
        
    @staticmethod
    def notFound(values=None, error="Not Found"):
        return CustomResponse().base(values=values, error=error, isSuccess=False, status=404)

    @staticmethod
    def badRequest(values=None, error="Bad Request"):
        return CustomResponse().base(values=values, error=error, isSuccess=False, status=400)