FROM rabbitmq:3.8.1-management-alpine

LABEL maintainer = "Andrey Romanov"

COPY ./docker/rabbitmq/cluster-connect.sh /cluster-connect.sh
COPY ./docker/rabbitmq/root-init.sh /root-init.sh
COPY ./docker/rabbitmq/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]