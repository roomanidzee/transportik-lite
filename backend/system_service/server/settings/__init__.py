# -*- coding: utf-8 -*-

from split_settings.tools import include

base_settings = [
    'components/api.py',
    'components/caches.py',
    'components/celery.py',
    'components/common.py',
    'components/logging.py',
    'environments/development.py'
]

include(*base_settings)
