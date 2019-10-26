import typing

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from server.modules.security import services


@api_view(['POST'])
@permission_classes([AllowAny, ])
def register_user(request: Request) -> Response:
    """Endpoint for user registration"""

    register_result: typing.Dict = services.register(request.data)

    return Response(register_result, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request: Request) -> Response:
    """Endpoint for user authorize."""

    authorize_result: typing.Dict = services.authorize(request, request.data)

    return Response(authorize_result, status=status.HTTP_200_OK)
