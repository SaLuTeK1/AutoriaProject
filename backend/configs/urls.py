from django.urls import include, path

urlpatterns = [
    path('api/users', include('apps.users.urls')),
    path('api/auth', include('apps.auth.urls')),
]
