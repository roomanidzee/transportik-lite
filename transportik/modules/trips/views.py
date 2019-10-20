from rest_framework import viewsets

from transportik.modules.trips import serializers
from django_filters import rest_framework as dj_filters
from rest_framework.permissions import IsAuthenticated


class TripViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TripSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (dj_filters.DjangoFilterBackend,)
