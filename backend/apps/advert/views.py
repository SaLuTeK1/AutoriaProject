import json

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.pagination import PagePagination

from apps.advert.models import AdvertModel, AdvertViewsModel
from apps.advert.serializers import AdvertSerializer, AdvertStatsSerializer, CarPhotoSerializer
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer

from .filters import AdvertFilter


class CreateAdvertView(GenericAPIView):
    """
    Create a new advertisement
    """

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

        car_data = data.pop('car')
        car_serializer = CarSerializer(data=car_data)
        car_serializer.is_valid(raise_exception=True)

        car = car_serializer.save(user=user)

        advert_serializer.save(car=car)
        return Response(advert_serializer.data, status=status.HTTP_201_CREATED)


class UpdateAdvertView(GenericAPIView):
    """
    Update an existing advertisement
    """

    queryset = AdvertModel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AdvertSerializer

    def put(self, *args, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        advert_id = kwargs.get('pk')

        try:
            advert_instance = AdvertModel.objects.get(pk=advert_id, car__user=user)
        except AdvertModel.DoesNotExist:
            return Response(
                {"detail": "Advertisement not found or you do not have permission to edit this advertisement."},
                status=status.HTTP_404_NOT_FOUND
            )

        data = self.request.data
        advert_serializer = AdvertSerializer(advert_instance, data=data, partial=True)
        advert_serializer.is_valid(raise_exception=True)

        updated_advert = advert_serializer.save()

        if updated_advert.contains_prohibited_language(updated_advert.name) or updated_advert.contains_prohibited_language(updated_advert.info):
            return Response(
                {"detail": "Your advertisement contains prohibited language. Please correct it and try again."},
                status=status.HTTP_400_BAD_REQUEST
            )

        updated_advert.save()

        return Response(advert_serializer.data, status=status.HTTP_200_OK)


class ListAdvertView(ListAPIView):
    """
    Show all advertisements
    """
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertStatsSerializer
    permission_classes = (AllowAny,)
    filterset_class = AdvertFilter


class TestView(ListAPIView):
    """
    Show advertisement by id
    """

    permission_classes = (AllowAny,)
    queryset = AdvertModel.objects.all()
    serializer_class = AdvertStatsSerializer

    def get(self, *args, **kwargs):
        instance = self.get_object()
        AdvertViewsModel.objects.create(advert=instance)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class CarAddPhotoView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarPhotoSerializer
    http_method_names = ('put',)

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        profile: AdvertModel = self.get_object()
        profile.car_photo.delete()
        super().perform_update(serializer)

