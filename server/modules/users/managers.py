
from django.db import transaction
from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    """
    Manager for users of project
    """

    def _create_user(self, email: str, password: str, **extra_fields):
        """Save user with email and password"""

        if not email:
            raise ValueError('User must have an email')

        try:

            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except Exception as e:
            raise ValueError('Some error occured for user creation: {0}'.format(
                str(e)
            ))

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_super_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
