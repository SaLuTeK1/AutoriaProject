from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.permissions import IsManagerUser

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserBlock(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsManagerUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        sender = self.request.user
        if sender != user:
            if user.is_active:
                user.is_active = False
                user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUnBlock(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsManagerUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
