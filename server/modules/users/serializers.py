from rest_framework import serializers as srlz

from server.modules.users import models


class UserSerializer(srlz.ModelSerializer):
    """Serializer for user info"""
    created_date = srlz.ReadOnlyField()

    class Meta:
        model = models.User
        fields = ('id', 'email', 'password', 'created_date')
        extra_kwargs = {'password': {'write_only': True}}


class ProfileSerializer(srlz.ModelSerializer):
    """Serializer for profile info"""

    class Meta:
        model = models.Profile
        fields = '__all__'
