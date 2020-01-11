from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django_filters import rest_framework as dj_filters

from server.modules.users import serializers, filters


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (dj_filters.DjangoFilterBackend,)
    filterset_class = filters.UserFilter


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (dj_filters.DjangoFilterBackend,)
    filterset_class = filters.ProfileFilter
