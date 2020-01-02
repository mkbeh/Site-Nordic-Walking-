from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

from .category import Category

STATUS_CHOICES = (
    ('draft', 'Черновик'),
    ('published', 'Опубликовано')
)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = RichTextUploadingField(verbose_name='Текст поста')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')
    image = models.ImageField(upload_to='posts/%Y/%m/%d')

    category = models.ForeignKey(Category, models.PROTECT, verbose_name='Категория')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
