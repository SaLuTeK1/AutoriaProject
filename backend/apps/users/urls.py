from django.urls import path

from apps.users.views import UserBlock, UserListCreateAPIView, UserUnBlock

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='create-user'),
    path('/ban/<int:pk>', UserBlock.as_view(), name='ban-user'),
    path('/unban/<int:pk>', UserUnBlock.as_view(), name='unban-user'),
]