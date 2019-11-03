#!/usr/bin/env sh

set -o errexit
set -o nounset

python /code/manage.py migrate --noinput
python /code/manage.py collectstatic --noinput

/usr/local/bin/gunicorn server.wsgi \
  -w 4 \
  -b 0.0.0.0:8000 \
  --chdir=/code \
  --log-file=- \
  --worker-tmp-dir /dev/shm
