
from django.urls import path

from server.modules.security import views

urlpatterns = [
    path('register/', views.register_user),
    path('authorize/', views.authenticate_user)
]
