from rest_framework import viewsets

from transportik.modules.trips import serializers
from transportik.modules.transports import serializers as transport_srlz
from django_filters import rest_framework as dj_filters
from rest_framework.permissions import IsAuthenticated


class TripViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TripSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (dj_filters.DjangoFilterBackend,)


class TripInfoViewSet(viewsets.ModelViewSet):
    serializer_class = transport_srlz.TripInfoSerializer
    permission_classes = (IsAuthenticated,)
