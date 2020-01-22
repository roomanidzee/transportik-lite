
from django.urls import path

from server.modules.users import views

urlpatterns = [
    path('users/', views.UserViewSet),
    path('profiles/', views.ProfileViewSet),
]
