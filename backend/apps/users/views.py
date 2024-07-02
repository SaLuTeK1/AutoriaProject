
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from core.permissions import IsPremiumUser

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsPremiumUser,)
