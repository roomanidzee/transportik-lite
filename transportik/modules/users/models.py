from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.utils import timezone
from django.db import models

from transportik.modules.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'

    def __str__(self):
        return 'User(id = {0}, username = {1}, email = {2}, is_active = {3})'.format(
            self.id, self.get_username(), self.email, self.is_active
        )


class Profile(models.Model):

    phone_regex = RegexValidator(
        regex=r'^((\+7|7|8)+([0-9]){10})$',
        message='Regexp for phone number'
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    phone = models.CharField(
        validators=[phone_regex],
        max_length=12,
        blank=False
    )

    class Meta:
        db_table = 'profiles'

    def __str__(self):
        return 'Profile(id = {0}, surname = {1}, name = {2}, patronymic = {3}, phone = {4})'.format(
            self.id, self.surname, self.name, self.patronymic, self.phone
        )
