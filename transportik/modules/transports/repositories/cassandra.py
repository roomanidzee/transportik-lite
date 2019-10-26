from typing import List

from transportik.modules.transports.models import TransportAnalysis
from transportik.modules.transports.repositories.base import BaseAnalysisRepository
from transportik.settings.components import config
from transportik.settings.components.cassandra import CASSANDRA_CLUSTER


class CassandraAnalysisRepository(BaseAnalysisRepository):

    def __init__(self):
        super().__init__()

        self.keyspace = config['cassandra']['keyspace']
        self.table_name = config['cassandra']['table_name']

        self.session = CASSANDRA_CLUSTER.connect(self.keyspace)

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
            "INSERT INTO {keyspace}.{table_name}({fields}) VALUES({fields_count})".format(
                keyspace=self.keyspace,
                table_name=self.table_name,
                fields=','.join(self.fields),
                fields_count=['?' for _ in range(len(self.fields))]
            )
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
        pass

    def delete(self, identifier):
        pass
