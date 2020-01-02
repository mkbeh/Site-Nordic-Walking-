from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


class Instructor(models.Model):
    initials = models.CharField(max_length=100, unique=True, verbose_name='Инициалы')
    contacts = RichTextUploadingField(verbose_name='Подробная информация')
    image = models.ImageField(verbose_name='Фото', blank=True, upload_to='instructors/%Y/%m/%d')

    class Meta:
        verbose_name = 'Инструктор'
        verbose_name_plural = 'Инструкторы'

    def __str__(self):
        return self.initials
