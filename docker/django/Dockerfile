FROM python:3.7.5-slim-stretch as development_build

LABEL maintainer = "Andrey Romanov"

ARG DJANGO_ENV
ARG DOCKERIZE_VERSION
ARG POETRY_VERSION

ENV DJANGO_ENV=${DJANGO_ENV} \
    DOCKERIZE_VERSION=${DOCKERIZE_VERSION} \
    POETRY_VERSION=${POETRY_VERSION} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt update && apt install -y --no-install-recommends gettext python3-dev libpq-dev netcat g++ gcc wget

RUN pip install poetry \
    && wget "https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-alpine-linux-amd64-v0.6.1.tar.gz" \
    && tar -C /usr/local/bin -xzvf "dockerize-alpine-linux-amd64-v0.6.1.tar.gz" \
    && rm "dockerize-alpine-linux-amd64-v0.6.1.tar.gz"

WORKDIR /pysetup
COPY ./poetry.lock ./pyproject.toml /pysetup/

COPY ./docker/django/entrypoint.sh /docker-entrypoint.sh

RUN chmod +x "/docker-entrypoint.sh" \
  && poetry config settings.virtualenvs.create false \
  && poetry install

WORKDIR /code

ENTRYPOINT ["/docker-entrypoint.sh"]