from transportik.settings.components import config
from cassandra.cluster import Cluster

CASSANDRA_CLUSTER = Cluster(
    contact_points=config['cassandra']['contact_points'],
    port=config['cassandra']['port']
)
