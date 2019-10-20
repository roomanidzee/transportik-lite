
from django.contrib.gis import admin

from transportik.modules.trips.models import Trip


@admin.register(Trip)
class TripAdmin(admin.OSMGeoAdmin):
    list_display = ('source', 'target')
