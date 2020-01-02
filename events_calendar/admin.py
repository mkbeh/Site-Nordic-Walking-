from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date_from', 'event_date_to', 'created')
    list_filter = ('event_date_from', 'created')
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
