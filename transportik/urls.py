# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('admin/doc/', include(admindocs_urls)),
    path('admin/', admin.site.urls),
    path('api/v1/transportik/', include('transportik.modules.urls')),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar   # noqa: WPS433
    from django.conf.urls.static import static  # noqa: WPS433

    urlpatterns = (
        [path('__debug__/', include(debug_toolbar.urls))]  # noqa: DJ05
        + urlpatterns
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )


