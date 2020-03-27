from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration
from django.utils.timezone import localtime
import pytz
from django.conf import settings


def passcard_info_view(request, passcode):
    tz = pytz.timezone(settings.TIME_ZONE)
    passcard = Passcard.objects.filter(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in passcard_visits:
        entered_at = localtime(value=visit.entered_at, timezone=tz)
        leaved_at = localtime(value=visit.leaved_at, timezone=tz)
        this_passcard_visit = {
            "entered_at": visit.entered_at.strftime('%d %B %Y  %H:%M'),
            "duration": format_duration(visit.get_duration()),
            "is_strange": False,
        }
        this_passcard_visits.append(this_passcard_visit)
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
