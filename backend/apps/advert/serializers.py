from datetime import datetime, timedelta

from rest_framework import serializers

from apps.cars.serializers import CarSerializer

from .models import AdvertModel


class AdvertSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = AdvertModel
        fields = ('id', 'name', 'info', 'status', 'edit_attempts', 'car')
        read_only_fields = ('id', 'status', 'edit_attempts')


class AdvertStatsSerializer(serializers.ModelSerializer):
    views_last_day = serializers.SerializerMethodField()
    views_last_week = serializers.SerializerMethodField()
    views_last_month = serializers.SerializerMethodField()
    avg_price_region = serializers.SerializerMethodField()
    avg_price_country = serializers.SerializerMethodField()

    class Meta:
        model = AdvertModel
        fields = [
            'views',
            'views_last_day',
            'views_last_week',
            'views_last_month',
            'avg_price_region',
            'avg_price_country']

    read_only_fields = ('views',
                        'views_last_day',
                        'views_last_week',
                        'views_last_month',
                        'avg_price_region',
                        'avg_price_country')

    def get_views_last_day(self, obj):
        return obj.views_set.filter(timestamp__gte=datetime.now() - timedelta(days=1)).count()

    def get_views_last_week(self, obj):
        return obj.views_set.filter(timestamp__gte=datetime.now() - timedelta(days=7)).count()

    def get_views_last_month(self, obj):
        return obj.views_set.filter(timestamp__gte=datetime.now() - timedelta(days=30)).count()

    def get_avg_price_region(self, obj):
        region_ads = AdvertModel.objects.filter(region=obj.region)
        total_price = sum(ad.price for ad in region_ads)
        return total_price / len(region_ads) if region_ads.exists() else 0

    def get_avg_price_country(self, obj):
        all_ads = AdvertModel.objects.all()
        total_price = sum(ad.price for ad in all_ads)
        return total_price / len(all_ads) if all_ads.exists() else 0
