from rest_framework import serializers as srlz

from server.modules.transports import models


class TransportInfoSerializer(srlz.ModelSerializer):
    """Serializer for transport info"""

    class Meta:
        model = models.TransportInfo
        fields = '__all__'


class TransportPositionSerializer(srlz.ModelSerializer):
    """Serializer for transport position"""

    class Meta:
        model = models.TransportPosition
        fields = '__all__'


class TripInfoSerializer(srlz.ModelSerializer):
    """Serializer for trip info"""

    class Meta:
        model = models.TripInfo
        fields = '__all__'
