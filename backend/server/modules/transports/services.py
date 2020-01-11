
import logging

import pika
from pika.adapters.blocking_connection import BlockingChannel

from server.settings.components import config

logger = logging.getLogger(__name__)

rabbit_conf = config['rabbitmq']

creds = pika.PlainCredentials(
        username=rabbit_conf['user'],
        password=rabbit_conf['password']
)

conn_parameters = pika.ConnectionParameters(
    host=rabbit_conf['host'],
    port=rabbit_conf['port'],
    credentials=creds
)

connection = pika.BlockingConnection(conn_parameters)
channel: BlockingChannel = connection.channel()


def produce_transports(limit: int):

    for i in range(limit):

        channel.basic_publish(
            exchange='transports',
            routing_key='test_message',
            body=bytes(f'test_message_{i}', 'utf-8')
        )


def consume_transports():

    for method_frame, _, body in channel.consume('transports'):

        logger.info(f'MESSAGE: {body}')
        channel.basic_ack(method_frame.delivery_tag)
