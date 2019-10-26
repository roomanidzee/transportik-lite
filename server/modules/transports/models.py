from datetime import datetime
from dataclasses import dataclass

from django.contrib.gis.db import models
from django.utils import timezone

from server.modules.transports.enums import TransportType
from server.modules.trips.models import Trip


@dataclass
class TransportAnalysis(object):
    record_time: datetime
    transport_id: int
    is_busy: bool
    is_repairing: bool
    trip_id: int
    distance: int
    cost: int


class TransportInfo(models.Model):
    """Entity for transport info."""

    name = models.CharField(max_length=100)
    length = models.IntegerField()
    tonnage = models.IntegerField()
    created_time = models.DateTimeField(default=timezone.now)
    type = models.IntegerField(
        choices=[
            (elem, elem.value)
            for elem in TransportType
        ]
    )

    class Meta:
        db_table = 'transport_info'

    def __str__(self):
        return 'TransportInfo(id = {0}, length = {1}, tonnage = {2}, created_time = {3}, type = {4})'.format(
            self.id, self.length, self.tonnage, self.created_time, self.type
        )


class TransportPosition(models.Model):
    """Entity for transport position."""

    transport = models.ForeignKey(
        TransportInfo,
        db_column='transport_id',
        null=True,
        on_delete=models.SET_NULL
    )

    coordinate = models.PointField()

    record_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'transport_position'

    def __str__(self):
        return 'TransportPosition(id = {0}, transport_id = {1}, coordinate = {2}, record_date = {3})'.format(
            self.id, self.transport_id, self.coordinate, self.record_date
        )


class TripInfo(models.Model):
    """Entity for trip information"""

    trip = models.ForeignKey(
        Trip,
        db_column='trip_id',
        null=True,
        on_delete=models.SET_NULL
    )

    transport = models.ForeignKey(
        TransportInfo,
        db_column='transport_id',
        null=True,
        on_delete=models.SET_NULL
    )

    cost = models.IntegerField()

    class Meta:
        db_table = 'trip_info'

    def __str__(self):
        return 'TripInfo(id = {0}, trip_id = {1}, transport_id = {2}, cost = {3})'.format(
            self.id, self.trip.id, self.transport.id, self.cost
        )
