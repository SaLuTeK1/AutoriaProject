from django.urls import path

from apps.cars.views import CarListView, CarRetrieveUpdateDestroyView, CreateCarView

urlpatterns = [
    path('', CarListView.as_view(), name='cars'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars-change'),
    path('/create', CreateCarView.as_view(), name='cars-create'),
]