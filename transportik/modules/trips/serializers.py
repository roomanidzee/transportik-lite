from rest_framework import serializers as srlz

from transportik.modules.trips import models


class TripSerializer(srlz.ModelSerializer):
    """Serializer for trip info."""

    class Meta:
        model = models.Trip
        fields = '__all__'
