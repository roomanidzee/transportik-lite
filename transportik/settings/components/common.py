# -*- coding: utf-8 -*-

from typing import Tuple

from django.utils.translation import ugettext_lazy as _

from transportik.settings.components import BASE_DIR, config

SECRET_KEY = config['secret_key']

# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (

    'transportik.modules',
    'transportik.modules.users',
    'transportik.modules.transports',
    'transportik.modules.trips',
    'transportik.modules.security',

    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # DRF
    'rest_framework',
    'rest_framework_gis',
    'django_filters',

    # PostGIS
    'django.contrib.gis'
)

MIDDLEWARE: Tuple[str, ...] = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'transportik.urls'

WSGI_APPLICATION = 'transportik.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': config['jdbc']['engine'],
        'NAME': config['jdbc']['name'],
        'USER': config['jdbc']['user'],
        'PASSWORD': config['jdbc']['password'],
        'HOST': config['jdbc']['host'],
        'PORT': config['jdbc']['port'],
        'CONN_MAX_AGE': config['jdbc']['conn_max_age'],
        'OPTIONS': {'connect_timeout': 10},
    },
}


LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

LANGUAGES = (('en', _('English')), ('ru', _('Russian')))

LOCALE_PATHS = ('locale/',)

USE_TZ = True
TIME_ZONE = 'UTC'


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath('static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('transportik', 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]
