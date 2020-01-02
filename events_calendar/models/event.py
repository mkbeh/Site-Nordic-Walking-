from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.text import slugify
from django.shortcuts import reverse

from ckeditor_uploader.fields import RichTextUploadingField


def get_date_with_reset_time(date):
    return timezone.datetime(date.year, date.month, date.day)


def get_filter_dates(days):
    return [
        get_date_with_reset_time(timezone.now() + timezone.timedelta(days=x))
        for x in range(days)
    ]


class EventQuerySet(models.QuerySet):
    def days_filtering(self, days):
        q = Q(event_date_from__gte=timezone.now()) | Q(event_date_to__gte=timezone.now())
        events = self.all().filter(q).order_by('event_date_from')

        filter_dates = get_filter_dates(days)
        filtered_events = []

        for event in events:
            if event.event_date_to:
                event_delta_days = (event.event_date_to - event.event_date_from).days

                if event_delta_days > 0:
                    event_dates = (get_date_with_reset_time(event.event_date_from + timezone.timedelta(days=x))
                                   for x in range(event_delta_days))
                else:
                    event_dates = (timezone.datetime(event.event_date_to.year,
                                                     event.event_date_to.month,
                                                     event.event_date_to.day), )
                for event_date in event_dates:
                    if event_date in filter_dates:
                        filtered_events.append(event)
                        break
            else:
                filtered_events.append(event)

        return filtered_events


class EventManager(models.Manager):
    def get_queryset(self):
        return EventQuerySet(self.model, using=self.db)

    def days_filtering(self, days):
        return self.get_queryset().days_filtering(days)


class Event(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название события')
    slug = models.SlugField(max_length=250)
    description = RichTextUploadingField(verbose_name='Описание события')
    event_date_from = models.DateTimeField(verbose_name='Дата события ОТ')
    event_date_to = models.DateTimeField(verbose_name='Дата события ДО', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=timezone.now(), verbose_name='Дата создания события')
    preview_image = models.ImageField(upload_to='events/%Y/%m/%d', verbose_name='Превью картинка')

    objects = models.Manager()
    events = EventManager()

    class Meta:
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('calendar:calendar_event_detail',
                       args=[self.created.year, self.created.month,
                             self.created.day, self.created.hour, self.slug])

    def __str__(self):
        return self.title
