from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField


TYPE_CHOICES = (
    ('photo', 'Фото'),
    ('video', 'Видео')
)


class Album(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название альбома')
    slug = models.SlugField(max_length=250)
    description = RichTextUploadingField(verbose_name='Описание альбома', blank=True)
    preview_photo = models.ImageField(upload_to='album/%Y/%m/%d', verbose_name='Превью картинка')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Тип альбома')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Album, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gallery:album_detail', args=[self.type, self.name])

    def __str__(self):
        return self.name


class PhotoAlbum(Album):
    class Meta:
        verbose_name = 'Фото альбом'
        verbose_name_plural = 'Фото альбомы'


class VideoAlbum(Album):
    class Meta:
        verbose_name = 'Видео альбом'
        verbose_name_plural = 'Видео альбомы'


class Images(models.Model):
    photo_album = models.ForeignKey(PhotoAlbum, on_delete=models.CASCADE, blank=True)
    file = models.ImageField(verbose_name='Изображение', upload_to='album/%Y/%m/%d')

    def __str__(self):
        return f'Изображение для альбома {self.photo_album.name}'


class Videos(models.Model):
    video_album = models.ForeignKey(VideoAlbum, on_delete=models.CASCADE, blank=True)
    file = EmbedVideoField(verbose_name='URL видео')

    def __str__(self):
        return f'URL видео для альбома {self.video_album.name}'
