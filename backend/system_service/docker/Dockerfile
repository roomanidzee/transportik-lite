FROM python:3.7-slim-buster as development_build

LABEL maintainer = "Andrey Romanov"

ARG DJANGO_ENV
ARG DJANGO_SETTINGS_MODULE
ARG DOCKERIZE_VERSION
ARG POETRY_VERSION
ARG PYSPARK_VERSION

ENV DJANGO_ENV=${DJANGO_ENV} \
    DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE} \
    DOCKERIZE_VERSION=${DOCKERIZE_VERSION} \
    POETRY_VERSION=${POETRY_VERSION} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update  \
    && apt-get install -y --no-install-recommends gettext python3-dev libpq-dev netcat g++ gcc wget \
                                              libgeos-dev binutils libproj-dev gdal-bin libgdal-dev python3-gdal

RUN pip install "poetry==$POETRY_VERSION" \
    && wget "https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
    && tar -C /usr/local/bin -xzvf "dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
    && rm "dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz"

WORKDIR /pysetup
COPY ./poetry.lock ./pyproject.toml /pysetup/

COPY ./docker/entrypoint.sh /docker-entrypoint.sh

RUN pip install "pyspark==$PYSPARK_VERSION"

RUN poetry config virtualenvs.create false \
  && poetry install

WORKDIR /code

ENTRYPOINT ["/docker-entrypoint.sh"]