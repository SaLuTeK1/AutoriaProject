from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.advert.models import AdvertModel
from apps.advert.serializers import AdvertSerializer
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CreateAdvertView(GenericAPIView):
    queryset = AdvertModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AdvertSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        print(user)
        advert_serializer = AdvertSerializer(data=self.request.data)
        advert_serializer.is_valid(raise_exception=True)
        car_data = self.request.data.pop('car')
        car_serializer = CarSerializer(data=car_data)
        car_serializer.is_valid(raise_exception=True)
        car = car_serializer.save()
        advert = advert_serializer.save(car=car)

        return Response(advert.data, status=status.HTTP_201_CREATED)

