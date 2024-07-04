from rest_framework import serializers

from apps.cars.models import CarModel


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
                  'price',)

    def validate(self, attrs):
        print(attrs)
        return attrs


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'price', 'year')
