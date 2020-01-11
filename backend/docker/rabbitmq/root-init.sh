#!/bin/bash

set -e

/usr/local/bin/docker-entrypoint.sh rabbitmq-server

VHOST=/
EXCHANGE=transports
USER=guest
PASS=guest
QUEUE=transports

# Enable admin

rabbitmq-plugins enable rabbitmq_management

curl http://localhost:15672/cli/rabbitmqadmin > /usr/local/sbin/rabbitmqadmin
chmod +x /usr/local/sbin/rabbitmqadmin

# Add queues

rabbitmqadmin -u${USER} -p${PASS} declare exchange --vhost=${VHOST} name=${EXCHANGE} type=direct durable=true

rabbitmqadmin -u${USER} -p${PASS} declare queue --vhost=${VHOST} name=${QUEUE} durable=true auto_delete=false

rabbitmqadmin -u${USER} -p${PASS} declare binding --vhost=${VHOST} source=${EXCHANGE} destination=${QUEUE}
