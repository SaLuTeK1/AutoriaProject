from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.pagination import PagePagination

from apps.advert.models import AdvertModel, AdvertViewsModel
from apps.advert.serializers import AdvertSerializer, AdvertStatsSerializer
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CreateAdvertView(GenericAPIView):
    queryset = AdvertModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AdvertSerializer

    def post(self, *args, **kwargs):
        user = self.request.user

        if not user.is_premium and CarModel.objects.filter(user=user).count() >= 1:
            return Response(
                {"detail": "You cannot add more than one advertisement with a basic account."},
                status=status.HTTP_403_FORBIDDEN
            )

        data = self.request.data
        advert_serializer = AdvertSerializer(data=data)
        advert_serializer.is_valid(raise_exception=True)

        car_data = self.request.data.pop('car')
        car_serializer = CarSerializer(data=car_data)
        car_serializer.is_valid(raise_exception=True)
        car = car_serializer.save(user=user)

        advert_serializer.save(car=car)
        return Response(advert_serializer.data, status=status.HTTP_201_CREATED)


class ListAdvertView(ListAPIView):
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertStatsSerializer
    permission_classes = (AllowAny,)
    pagination_class = PagePagination


class TestView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertStatsSerializer

    def get(self, *args, **kwargs):
        instance = self.get_object()
        AdvertViewsModel.objects.create(advert=instance)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
