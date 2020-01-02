from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name
