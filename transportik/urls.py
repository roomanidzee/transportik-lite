# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('api/v1/admin/doc/', include(admindocs_urls)),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/transportik/', include('transportik.modules.urls')),
]


