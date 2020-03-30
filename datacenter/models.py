from django.db import models
from django.utils.timezone import localtime
import pytz
from django.conf import settings


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at)
            if self.leaved_at else "not leaved"
        )

    def get_duration(self):
        tz = pytz.timezone(settings.TIME_ZONE)
        now = localtime(value=None, timezone=tz)
        if self.leaved_at:
            delta = self.leaved_at - self.entered_at
        else:
            delta = now - self.entered_at
        seconds = delta.total_seconds()
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return (hours, minutes)

    def is_long(self, limit=60):
        _, minutes = self.get_duration()
        return int(minutes) >= limit


def format_duration(duration):
    hours, minutes = duration
    return "{0}ч {1}мин".format(int(hours), int(minutes))
