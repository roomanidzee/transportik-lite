#!/usr/bin/env sh

set -o errexit
set -o nounset

postgres_ready () {
  dockerize -wait tcp://db:5432 -timeout 5s
}

until postgres_ready; do
  >&2 echo 'Postgres is unavailable - sleeping'
done

if [ "$1" = 'start-dev' ]; then
    python manage.py makemigrations;
    python manage.py migrate;
    python manage.py collectstatic;
    python manage.py runserver 0.0.0.0:8000
elif [ "$1" = 'start-prod' ]; then
    sh /code/docker/django/gunicorn.sh
elif [ "$1" = 'start-celery' ]; then
    celery -E -A server.settings worker -B --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=info
fi
