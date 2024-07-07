from django.urls import path

from apps.advert.views import CreateAdvertView, ListAdvertView, TestView

from .utils import get_region

urlpatterns = [
    path('/create', CreateAdvertView.as_view(), name='create-advert'),
    path('', ListAdvertView.as_view(), name='list-advert'),
    path('/<int:pk>', TestView.as_view(), name='ONE-advert'),
    path('/regions', get_region, name='get-regions')
]