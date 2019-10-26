# -*- coding: utf-8 -*-

from django.urls import include, path

urlpatterns = [
    path('security/', include('server.modules.security.urls')),
    path('accounts/', include('server.modules.users.urls')),
    path('transports/', include('server.modules.transports.urls')),
    path('trips/', include('server.modules.trips.urls'))
]
