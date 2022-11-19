
from django.db import models
from django.contrib.auth.models import AbstractUser
from user_auth.myusermanager import MyUserManager


class User(AbstractUser):
    username = None
    mobile = models.CharField(max_length=20, unique=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    backend = 'user_auth.mybackend.MobileBackend'

