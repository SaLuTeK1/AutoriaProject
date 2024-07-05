from datetime import datetime, timedelta

from rest_framework import serializers

from apps.advert.models import AdvertModel, AdvertViewsModel
from apps.cars.serializers import CarSerializer


class AdvertSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = AdvertModel
        fields = ('id', 'name', 'info', 'status', 'edit_attempts', 'car')
        read_only_fields = ('id', 'status', 'edit_attempts')


class AdvertStatsSerializer(serializers.ModelSerializer):
    views_last_day = serializers.SerializerMethodField()
    # views_last_week = serializers.SerializerMethodField()
    # views_last_month = serializers.SerializerMethodField()
    avg_price_region = serializers.SerializerMethodField()
    avg_price_country = serializers.SerializerMethodField()

    class Meta:
        model = AdvertModel
        fields = ['id', 'name', 'info', 'status', 'views', 'edit_attempts', 'views_last_day', 'avg_price_region',
                  'avg_price_country', 'car']
        read_only_fields = ('id', 'status', 'edit_attempts')

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
