from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel

from apps.users.managers import UserManager


# Create your models here.
class UserModel(PermissionsMixin, AbstractBaseUser, BaseModel):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=128, validators=[
        V.RegexValidator(*RegexEnum.PASSWORD.value)
    ])

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=30, validators=[
        V.RegexValidator(*RegexEnum.NAME.value)
    ])

    surname = models.CharField(max_length=30, validators=[
        V.RegexValidator(*RegexEnum.NAME.value)
    ])

    age = models.IntegerField(validators=[V.MaxValueValidator(100)])

    phone = models.CharField(max_length=30, validators=[
        V.RegexValidator(*RegexEnum.PHONE.value)
    ])

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
   

