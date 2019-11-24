# -*- coding: utf-8 -*-

from celery import Celery
from celery.schedules import crontab

from server.modules.transports.tasks import (
    send_transports_task,
    retrieve_transports,
)
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

tasks_data = [
    (
        crontab(minute=2),
        send_transports_task.s(),
        1
    ),
    (
        crontab(minute=4),
        retrieve_transports.s(),
        1
    )
]


@app.on_after_configure.connect
def setup_tasks(sender, **kwargs):
    for elem in tasks_data:
        sender.add_periodic_task(
            elem[0],
            elem[1],
            expires=elem[2]
        )

