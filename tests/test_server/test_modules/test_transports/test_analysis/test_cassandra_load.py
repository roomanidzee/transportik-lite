import random
from datetime import datetime

from server.modules.transports.models import TransportAnalysis
from server.modules.transports.repositories.cassandra import CassandraAnalysisRepository


def test_load(test_settings):
    cassandra_repo = CassandraAnalysisRepository(test_settings)

    for _ in range(1_000_000):
        cassandra_repo.save(
            TransportAnalysis(
                record_time=datetime.now(),
                transport_id=random.randrange(1, 100),
                is_busy=random.choice([True, False]),
                is_repairing=random.choice([True, False]),
                trip_id=random.randrange(1, 100),
                distance=random.randrange(1, 100000),
                cost=random.randrange(1, 100000)
            )
        )
