
from server.settings.components.celery import app


@app.task
def send_transports():
    print("HEY!")
