from django.urls import path

from .views import events_calendar, calendar_event_detail, past_competitions


app_name = 'events_calendar'

urlpatterns = [
    path('past_competitions/', past_competitions, name='past_competitions'),
    path('<int:year>/<int:month>/<int:day>/<int:hour>/<slug:event>/',
         calendar_event_detail, name='calendar_event_detail'),
    path('<int:days>', events_calendar, name='events_calendar'),
]
