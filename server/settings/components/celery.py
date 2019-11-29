# -*- coding: utf-8 -*-

from celery import Celery
from server.settings.components import config

redis_conf = config['redis']
redis_url = f'redis://{redis_conf["host"]}: {redis_conf["port"]}/{redis_conf["db"]}'


class Config:
    broker_url = redis_url
    result_backend = redis_url
    broker_api = redis_url
    accept_content = ['pickle', 'json']
    task_track_started = True
    imports = [
        "server.modules.transports.tasks"
    ]


app = Celery()
app.config_from_object(Config)

app.conf.beat_schedule = {
    'transports_producing': {
        'task': 'server.modules.transports.tasks.send_transports_task',
        'schedule': 10.0
    },
    'transports_consuming': {
        'task': 'server.modules.transports.tasks.retrieve_transports',
        'schedule': 20.0
    }
}
