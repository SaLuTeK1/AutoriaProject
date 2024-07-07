from datetime import datetime

from django.conf import settings
from django.core import validators as V
from django.core.exceptions import ValidationError
from django.db import models

from core.models import BaseModel

from apps.cars.choises import CAR_MODELS, BrandChoices, CarChoices, CurrencyChoices

from .tasks import get_exchange_rates


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars')

    brand = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)], choices=[*BrandChoices.choices])
    model = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(datetime.now().year)])

    engine = models.FloatField(validators=[V.MinValueValidator(0.1)])
    fuel = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    body_type = models.CharField(max_length=20, choices=[*CarChoices.choices])
    drive = models.CharField(max_length=20, validators=[V.MinLengthValidator(2)])
    gearbox = models.CharField(max_length=23, validators=[V.MinLengthValidator(2)])
    capacity = models.IntegerField(validators=[V.MinValueValidator(1)])
    mileage = models.IntegerField(validators=[V.MinValueValidator(1)])

    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(5000000)])
    currency = models.CharField(max_length=3, choices=[*CurrencyChoices.choices])

    price_usd = models.FloatField(blank=True, null=True)
    price_eur = models.FloatField(blank=True, null=True)
    price_uah = models.FloatField(blank=True, null=True)
    exchange_rate_usd = models.FloatField(blank=True, null=True)
    exchange_rate_eur = models.FloatField(blank=True, null=True)
    exchange_rate_uah = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):

        if self.currency and self.price:
            rates = get_exchange_rates()
            self.exchange_rate_usd = rates['USD']
            self.exchange_rate_eur = rates['EUR']
            self.exchange_rate_uah = rates['UAH']

            if self.currency == 'USD':
                self.price_usd = self.price
                self.price_eur = self.price * self.exchange_rate_usd / self.exchange_rate_eur
                self.price_uah = self.price * self.exchange_rate_usd / self.exchange_rate_uah
            elif self.currency == 'EUR':
                self.price_eur = self.price
                self.price_usd = self.price * self.exchange_rate_eur / self.exchange_rate_usd
                self.price_uah = self.price * self.exchange_rate_eur / self.exchange_rate_uah
            elif self.currency == 'UAH':
                self.price_uah = self.price
                self.price_usd = self.price * self.exchange_rate_uah / self.exchange_rate_usd
                self.price_eur = self.price * self.exchange_rate_uah / self.exchange_rate_eur

        super().save(*args, **kwargs)
