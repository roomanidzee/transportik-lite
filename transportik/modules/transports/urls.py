from django.urls import path

from transportik.modules.transports import views

urlpatterns = [
    path('info/', views.TransportInfoViewSet),
    path('positions/', views.TransportPositionViewSet),
]