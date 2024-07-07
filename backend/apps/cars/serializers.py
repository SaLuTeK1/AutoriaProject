from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel

from .choises import CAR_MODELS


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id',
                  'brand',
                  'model',
                  'year',
                  'engine',
                  'fuel',
                  'body_type',
                  'drive',
                  'gearbox',
                  'capacity',
                  'price',
                  'mileage',
                  'currency',)

    fuel = serializers.CharField(required=False)
    gearbox = serializers.CharField(required=False)

    def validate(self, attrs):
        brand = attrs.get('brand')
        model = attrs.get('model')

        if model not in CAR_MODELS.get(brand, []):
            raise ValidationError(f"The model '{model}' is not valid for brand '{brand}'")

        return attrs


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'price', 'year')
