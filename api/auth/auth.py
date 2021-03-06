from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models


class Auth(BaseAuthentication):

    def authenticate(self, request):
        token = request.data.get('token')
        obj = models.UserToken.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed({'code': 1001, 'error': '认证失败'})
        return (obj.user, obj)
