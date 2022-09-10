from functools import wraps

import jwt
from apps.jwt import JWTAuth
from .custom_response import CustomResponse
from rest_framework.exceptions import AuthenticationFailed


def jwtRequired(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            raise AuthenticationFailed('Unauthorization access')
        try:
            decode(token)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token Expired')
        except jwt.InvalidSignatureError:
            raise AuthenticationFailed('Invalid Token')
        except Exception as e:
            raise AuthenticationFailed(e)
        return func(self, request, *args, **kwargs)
    return wrapper

def decode(token):
    token = str(token).split(' ')
    return JWTAuth().decode(token[1])