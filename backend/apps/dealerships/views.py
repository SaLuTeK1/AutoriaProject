from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.permissions import IsPremiumUser

from .serializers import DealershipSerializer


# Create your views here.
class DealershipCreateView(GenericAPIView):
    """
    Create a new dealership
    """
    serializer_class = DealershipSerializer
    permission_classes = (IsPremiumUser,) #тут можна добавити логіку який саме юзер може створити

    def post(self, *args, **kwargs):
        user = self.request.user

        if not user.is_premium:
            return Response(
                {"detail": "You cannot create own car dealership."},
                status=status.HTTP_403_FORBIDDEN
            )

        data = self.request.data.copy()
        data['user'] = user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
