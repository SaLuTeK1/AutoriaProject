from datetime import datetime

from django.conf import settings
from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.cars.choises import CarChoices, DriveChoices, FuelChoices, GearBoxes


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars')

    brand = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    model = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(datetime.now().year)])

    engine = models.FloatField()
    fuel = models.CharField(max_length=20, choices=[*FuelChoices.choices])
    body_type = models.CharField(max_length=20, choices=[*CarChoices.choices])
    drive = models.CharField(max_length=20, choices=[*DriveChoices.choices])
    gearbox = models.CharField(max_length=23, choices=[*GearBoxes.choices])
    capacity = models.IntegerField(validators=[V.MinValueValidator(1)])

    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(5000000)])

