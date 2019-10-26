
from django.contrib.gis import admin

from server.modules.trips.models import Trip


@admin.register(Trip)
class TripAdmin(admin.OSMGeoAdmin):
    list_display = ('source', 'target')
