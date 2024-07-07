from django.urls import path

from .consumers import AdvertConsumer

websocket_urlpatterns = [
    path('', AdvertConsumer.as_asgi()),
]