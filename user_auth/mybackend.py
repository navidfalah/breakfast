from django.contrib.auth.backends import ModelBackend
from .models import User


class MobileBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        mobile = ''
        if 'mobile' in kwargs:
            mobile = kwargs['mobile']
        elif 'username' in kwargs:
            mobile = kwargs['username']
        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            pass

