from django_filters import rest_framework as filters

from transportik.modules.users import models


class UserFilter(filters.FilterSet):

    class Meta:
        model = models.User
        fields = '__all__'


class ProfileFilter(filters.FilterSet):

    class Meta:
        model = models.Profile
        fields = '__all__'
