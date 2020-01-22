from django.contrib.gis.db import models

from server.modules.users.models import Profile


class Trip(models.Model):
    """
    Entity for trip model
    """

    source = models.PointField()
    target = models.PointField()

    class Meta:
        db_table = 'trips'

    def __str__(self):
        return 'Trip(id = {0}, source = {1}, target = {2})'.format(
            self.id, self.source, self.target
        )


class TripToProfile(models.Model):
    """
    Entity for trip and profile relation
    """

    trip = models.ForeignKey(
        Trip,
        db_column='trip_id',
        null=True,
        on_delete=models.SET_NULL
    )

    profile = models.ForeignKey(
        Profile,
        db_column='profile_id',
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'trip_to_profile'

    def __str__(self):
        return 'TripToProfile(id = {0}, trip_id = {1}, profile_id = 2'.format(
            self.id, self.trip.id, self.profile.id
        )

