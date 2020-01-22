import random
from datetime import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from server.modules.transports.models import TransportAnalysis
from server.settings.components import config
from server.modules.transports import serializers
from server.modules.transports.repositories.cassandra import CassandraAnalysisRepository


class TransportInfoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransportInfoSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'], url_path='load_data')
    def create_test_load(self, request: Request, pk: int) -> Response:

        # здесь инициализация сериализатора в будущем
        print("add serializer in future")
        cassandra_repo = CassandraAnalysisRepository(config)

        for _ in range(1_000_000):
            cassandra_repo.save(
                TransportAnalysis(
                    record_time=datetime.now(),
                    transport_id=pk,
                    is_busy=random.choice([True, False]),
                    is_repairing=random.choice([True, False]),
                    trip_id=random.randrange(1, 100),
                    distance=random.randrange(1, 100000),
                    cost=random.randrange(1, 100000)
                )
            )

        return Response(data={
            'success': True
        })


class TransportPositionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransportPositionSerializer
    permission_classes = (IsAuthenticated,)

