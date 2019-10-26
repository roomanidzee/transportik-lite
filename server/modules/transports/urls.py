from django.urls import path

from server.modules.transports import views

urlpatterns = [
    path('info/', views.TransportInfoViewSet),
    path('positions/', views.TransportPositionViewSet),
]