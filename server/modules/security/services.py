import typing

import jwt
import bcrypt

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.signals import user_logged_in
from rest_framework.request import Request
from rest_framework_jwt.utils import jwt_payload_handler

from server.modules.users import serializers as user_srlz
from server.modules.security import serializers as security_srlz
from server.modules.users.models import User


def register(user_data: typing.Dict) -> typing.Dict:
    """Registration of new user."""

    serializer = user_srlz.UserSerializer(data=user_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.validated_data


def authorize(request: Request, user_data: typing.Dict) -> typing.Dict:
    """Authorize user in service."""

    serializer = security_srlz.AuthSerializer(data=user_data)
    serializer.is_valid(raise_exception=True)

    srlz_data = serializer.validated_data

    try:
        existed_user = User.objects.get(email=srlz_data['email'])
    except ObjectDoesNotExist:
        raise ValueError('No user with email = {0}'.format(srlz_data['email']))

    payload = jwt_payload_handler(existed_user)
    payload['hashed_pw'] = bcrypt.hashpw(srlz_data['password'], bcrypt.gensalt())

    token = jwt.encode(payload, settings.SECRET_KEY)

    user_logged_in.send(sender=existed_user.__class__, request=request, user=existed_user)

    return {
        'token': token,
        'email': srlz_data['email']
    }
