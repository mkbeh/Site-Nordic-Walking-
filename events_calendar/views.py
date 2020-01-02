from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.db.models import Q

from blog.utils import get_pagination_page
from .models import Event


def calendar_event_detail(request, year, month, day, hour, event):
    event_obj = get_object_or_404(
        Event,
        slug=event,
        created__year=year,
        created__month=month,
        created__day=day,
        created__hour=hour
    )

    return render(request, 'calendar/event_detail.html', {'event': event_obj})


@cache_page(15*60)
def events_calendar(request, days=7):
    events = Event.events.days_filtering(days)
    page = get_pagination_page(request, events)

    return render(request, 'calendar/events_calendar.html', {'events': page.object_list, 'page': page})


@cache_page(15*60)
def past_competitions(request):
    q = Q(event_date_to__lt=timezone.now()) | Q(event_date_to=None)
    competitions = Event.objects.all().\
        filter(event_date_from__lt=timezone.now()).\
        filter(q).\
        order_by('event_date_from')

    page = get_pagination_page(request, competitions)
    return render(request, 'calendar/past_competitions.html', {'past_competitions': page.object_list, 'page': page})
