from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.advert.models import AdvertModel
from apps.users.models import UserModel


class DealershipModel(BaseModel):
    class Meta:
        db_table = 'dealerships'

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='dealership_user')
    name = models.CharField(max_length=30, validators=[
        V.MinLengthValidator(1)
    ])

    dealership_managers = models.ManyToManyField(UserModel, blank=True, related_name='dealership_managers')
    dealership_admins = models.ManyToManyField(UserModel, blank=True, related_name='dealership_admins')

    dealership_adverts = models.ManyToManyField(AdvertModel, blank=True, related_name='dealership_adverts')
