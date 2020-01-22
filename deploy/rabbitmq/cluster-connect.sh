#!/bin/bash

set -e

/usr/local/bin/docker-entrypoint.sh rabbitmq-server -detached

rabbitmqctl stop_app
rabbitmqctl join_cluster rabbit@tl_rabbit_1
rabbitmqctl stop

sleep 2s

rabbitmq-server