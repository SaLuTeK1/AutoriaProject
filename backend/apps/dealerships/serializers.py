
from rest_framework import serializers

from apps.advert.serializers import AdvertSerializer

from .models import DealershipModel


class DealershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = DealershipModel
        fields = ('id', 'name', 'user', 'dealership_managers', 'dealership_admins',  'dealership_adverts')
        read_only_fields = ('id', 'dealership_managers', 'dealership_admins')

