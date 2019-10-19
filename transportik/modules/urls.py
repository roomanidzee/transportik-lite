# -*- coding: utf-8 -*-

from django.urls import include, path

urlpatterns = [
    path('security/', include('transportik.modules.security.urls')),
    path('users/', include('transportik.modules.users.urls')),
    path('transports/', include('transportik.modules.transports.urls')),
    path('trips/', include('transportik.modules.trips.urls'))
]
