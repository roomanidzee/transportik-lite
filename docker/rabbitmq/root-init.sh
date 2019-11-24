#!/bin/bash

set -e

/usr/local/bin/docker-entrypoint.sh rabbitmq-server

VHOST=tl_vhost
EXCHANGE=transports
ADMIN_USER=admin
ADMIN_PASS=secret
JUST_USER=tl_user
JUST_PASS=tl_pass
QUEUE=transports

# Enable admin

rabbitmq-plugins enable rabbitmq_management

curl http://localhost:15672/cli/rabbitmqadmin > /usr/local/sbin/rabbitmqadmin
chmod +x /usr/local/sbin/rabbitmqadmin

# Add users

rabbitmqctl add_vhost ${VHOST}

rabbitmqctl add_user ${ADMIN_USER} ${ADMIN_PASS}
rabbitmqctl add_user ${JUST_USER} ${JUST_PASS}

rabbitmqctl set_user_tags ${ADMIN_USER} administrator
rabbitmqctl set_user_tags ${JUST_USER} management

rabbitmqctl set_permissions -p ${VHOST} ${ADMIN_USER} ".*" ".*" ".*"
rabbitmqctl set_permissions -p ${VHOST} ${JUST_USER} ".*" ".*" ".*"

# Add queues

rabbitmqadmin -u${ADMIN_USER} -p${ADMIN_PASS} declare exchange --vhost=${VHOST} name=${EXCHANGE} type=direct durable=true

rabbitmqadmin -u${ADMIN_USER} -p${ADMIN_PASS} declare queue --vhost=${VHOST} name=${QUEUE} durable=true auto_delete=false

rabbitmqadmin -u${ADMIN_USER} -p${ADMIN_PASS} declare binding --vhost=${VHOST} source=${EXCHANGE} destination=${QUEUE}
