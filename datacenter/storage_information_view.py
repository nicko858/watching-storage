from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import format_duration
from django.conf import settings
import pytz
import locale
locale.setlocale(locale.LC_TIME, settings.LOCALE)


def storage_information_view(request):
    tz = pytz.timezone(settings.TIME_ZONE)
    non_closed_visits_raw = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in non_closed_visits_raw:
        entered_at = localtime(value=visit.entered_at, timezone=tz)
        formatted_duration = format_duration(visit.get_duration())
        non_closed_visit = {
            "who_entered": visit.passcard,
            "entered_at": entered_at.strftime('%d %B %Y  %H:%M'),
            "duration": formatted_duration,
        }
        non_closed_visits.append(non_closed_visit)
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
