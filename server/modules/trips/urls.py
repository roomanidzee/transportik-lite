from django.urls import path

from server.modules.trips import views

urlpatterns = [
    path('info/', views.TripViewSet),
    path('history/', views.TripInfoViewSet)
]
