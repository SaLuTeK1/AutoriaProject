from django.urls import path

from channels.routing import URLRouter

from apps.advert.routing import websocket_urlpatterns as adverts_routing

websocket_urlpatterns = [
    path('api/adverts/', URLRouter(adverts_routing)),
]