from django.urls import path

from .views import DealershipCreateView

urlpatterns = [
    path('/create', DealershipCreateView.as_view(), name='create-advert'),

]