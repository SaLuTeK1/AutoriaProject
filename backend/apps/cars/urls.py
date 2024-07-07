from django.urls import path

from apps.cars.views import CarListView, CarRetrieveUpdateDestroyView, CreateCarView

from .utils import get_body_types, get_brands, get_models

urlpatterns = [
    path('', CarListView.as_view(), name='cars'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars-change'),
    path('/create', CreateCarView.as_view(), name='cars-create'),
    path('/brands', get_brands, name='get-car-brands'),
    path('/models', get_models),
    path('/bodies', get_body_types),

]
