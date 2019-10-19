from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
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
