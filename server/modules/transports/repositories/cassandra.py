from typing import Dict, List
from datetime import datetime

from cassandra.cluster import Cluster

from server.modules.transports.models import TransportAnalysis
from server.modules.transports.repositories.base import BaseAnalysisRepository


class CassandraAnalysisRepository(BaseAnalysisRepository):

    def __init__(self, config: Dict):
        super().__init__(config)

        cluster = Cluster(
            contact_points=self.config['cassandra']['contact_points'],
            port=self.config['cassandra']['port']
        )

        self.keyspace = self.config['cassandra']['keyspace']
        self.table_name = self.config['cassandra']['table_name']

        self.session = cluster.connect(self.keyspace)

    def find_all(self) -> List[TransportAnalysis]:
        result_set = self.session.execute('SELECT * FROM {0}'.format(self.table_name))

        return [
            TransportAnalysis(
                row.record_time,
                row.transport_id,
                row.is_busy,
                row.is_repairing,
                row.trip_id,
                row.distance,
                row.cost
            )
            for row in result_set
        ]

    def save(self, model: TransportAnalysis):
        insert_query = self.session.prepare(
            "INSERT INTO "
            "default.transport_analysis(record_time, transport_id, is_busy, is_repairing, trip_id, distance, cost) "
            "VALUES(?, ?, ?, ?, ?, ?, ?)"
        )

        self.session.execute(
            insert_query,
            [
                model.record_time,
                model.transport_id,
                model.is_busy,
                model.is_repairing,
                model.trip_id,
                model.distance,
                model.cost
            ]
        )

    def update(self, model: TransportAnalysis):

        update_query = self.session.prepare(
            "UPDATE default.transport_analysis "
            "SET record_time = ?, is_busy = ?, is_repairing = ?, trip_id = ?, distance = ?, cost = ?"
            "WHERE transport_id = ?"
        )

        self.session.execute(
            update_query,
            [
                model.record_time,
                model.is_busy,
                model.is_repairing,
                model.trip_id,
                model.distance,
                model.cost,
                model.transport_id
            ]
        )

    def delete(self, identifier: datetime):

        delete_query = self.session.prepare(
            "DELETE FROM default.transport_analysis "
            "WHERE record_time = blobAsBigint(timestampAsBlob(?))"
        )

        self.session.execute(
            delete_query,
            [identifier]
        )
