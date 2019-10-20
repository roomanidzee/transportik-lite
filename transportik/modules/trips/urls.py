from django.urls import path

from transportik.modules.trips import views

urlpatterns = [
    path('info/', views.TripViewSet),
    path('history/', views.TripInfoViewSet)
]
