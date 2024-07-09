from django.urls import path

from apps.advert.views import CarAddPhotoView, CreateAdvertView, GetAdvertView, ListAdvertView, UpdateAdvertView

from .utils import get_region

urlpatterns = [
    path('/create', CreateAdvertView.as_view(), name='create-advert'),
    path('/update/<int:pk>', UpdateAdvertView.as_view(), name='update-advert'),
    path('/add_photo/<int:pk>', CarAddPhotoView.as_view(), name='add-photo'),
    path('', ListAdvertView.as_view(), name='list-advert'),
    path('/<int:pk>', GetAdvertView.as_view(), name='ONE-advert'),
    path('/regions', get_region, name='get-regions')
]