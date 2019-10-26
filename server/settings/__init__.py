# -*- coding: utf-8 -*-

from split_settings.tools import include

base_settings = [
    'components/api.py',
    'components/caches.py',
    'components/common.py',
    'components/logging.py',
    'components/cassandra.py',
    'environments/development.py'
]

include(*base_settings)
