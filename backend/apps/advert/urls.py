from django.urls import path

from apps.advert.views import CreateAdvertView

urlpatterns = [
    path('', CreateAdvertView.as_view(), name='create-advert'),

]