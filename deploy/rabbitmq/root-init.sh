#!/bin/bash

set -e

/usr/local/bin/docker-entrypoint.sh rabbitmq-server

# Enable admin

rabbitmq-plugins enable rabbitmq_management

curl http://localhost:15672/cli/rabbitmqadmin > /usr/local/sbin/rabbitmqadmin
chmod +x /usr/local/sbin/rabbitmqadmin
