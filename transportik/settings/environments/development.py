# -*- coding: utf-8 -*-

from transportik.settings.components import config

DEBUG = True

ALLOWED_HOSTS = [config('domain'), 'localhost', '127.0.0.1', '[::1]']
