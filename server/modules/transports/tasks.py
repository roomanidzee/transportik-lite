
from server.settings.components.celery import app
from server.modules.transports.services import (
    produce_transports,
    consume_transports
)


@app.task
def send_transports_task():
    produce_transports(10_000)


@app.task
def retrieve_transports():
    consume_transports()
