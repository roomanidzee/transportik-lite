from rest_framework import serializers as srlz


class AuthSerializer(srlz.Serializer):
    """Serializer for user authorize"""
    email = srlz.CharField(max_length=100, required=True)
    password = srlz.CharField(max_length=100, required=True)
