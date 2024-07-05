from django.urls import path

from apps.advert.views import CreateAdvertView, TestView

urlpatterns = [
    path('', CreateAdvertView.as_view(), name='create-advert'),
    path('/<int:pk>', TestView.as_view(), name='ONE-advert'),

]