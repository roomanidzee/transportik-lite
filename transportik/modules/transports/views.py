from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from transportik.modules.transports import serializers


class TransportInfoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransportInfoSerializer
    permission_classes = (IsAuthenticated,)


class TransportPositionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransportPositionSerializer
    permission_classes = (IsAuthenticated,)

