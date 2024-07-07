from datetime import datetime, timedelta

from rest_framework import serializers

from apps.advert.models import AdvertModel, AdvertViewsModel
from apps.cars.serializers import CarSerializer

from .choises import RegionChoices


class AdvertSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = AdvertModel
        fields = ('id', 'name', 'info', 'region', 'status',  'car', 'car_photo')
        read_only_fields = ('id', 'status')

    info = serializers.CharField(required=False)
    car_photo = serializers.ImageField(required=False)
    region = serializers.ChoiceField(choices=RegionChoices.choices)

    def update(self, instance, validated_data):

        car_data = validated_data.pop('car', None)
        if car_data:
            car_serializer = CarSerializer(instance.car, data=car_data, partial=True)
            car_serializer.is_valid(raise_exception=True)
            car_serializer.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class AdvertStatsSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    views_last_day = serializers.SerializerMethodField()
    # views_last_week = serializers.SerializerMethodField()
    # views_last_month = serializers.SerializerMethodField()
    avg_price_region = serializers.SerializerMethodField()
    avg_price_country = serializers.SerializerMethodField()

    class Meta:
        model = AdvertModel
        fields = ['id', 'name', 'info', 'region', 'status', 'views',  'views_last_day', 'avg_price_region',
                  'avg_price_country', 'car']
        read_only_fields = ('id', 'status')

    def get_views_last_day(self, obj):
        return AdvertViewsModel.objects.filter(advert=obj, created_at__gte=datetime.now() - timedelta(days=1)).count()

    # def get_views_last_week(self, obj):
    #     return obj.views.filter(timestamp__gte=datetime.now() - timedelta(days=7)).count()
    #
    # def get_views_last_month(self, obj):
    #     return obj.views.filter(timestamp__gte=datetime.now() - timedelta(days=30)).count()

    def get_avg_price_region(self, obj):
        region_ads = AdvertModel.objects.filter(region=obj.region)
        total_price = sum(ad.car.price for ad in region_ads)
        return total_price / len(region_ads) if region_ads.exists() else 0

    def get_avg_price_country(self, obj):
        all_ads = AdvertModel.objects.all()
        total_price = sum(ad.car.price for ad in all_ads)
        return total_price / len(all_ads) if all_ads.exists() else 0
