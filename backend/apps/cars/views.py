from django.shortcuts import render

from rest_framework import status
# Create your views here.
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.cars.models import CarModel
from apps.cars.serializers import CarListSerializer, CarSerializer
from apps.users.models import ProfileModel, UserModel
from apps.users.serializers import UserSerializer


class CreateCarView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        data = self.request.data

        if not user.is_premium and CarModel.objects.filter(user=user).count() >= 1:
            return Response(
                {"detail": "You cannot add more than one car with a basic account."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CarListSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
