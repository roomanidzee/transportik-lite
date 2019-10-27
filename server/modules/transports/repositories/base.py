from typing import Dict

from server.modules.transports.models import TransportAnalysis


class BaseAnalysisRepository(object):

    def __init__(self, config: Dict):
        self.fields = ['record_time', 'transport_id', 'is_busy', 'is_repairing',
                       'trip_id', 'distance', 'cost']
        self.config = config

    def find_all(self):
        raise NotImplementedError

    def save(self, model: TransportAnalysis):
        raise NotImplementedError

    def update(self, model: TransportAnalysis):
        raise NotImplementedError

    def delete(self, identifier):
        raise NotImplementedError
