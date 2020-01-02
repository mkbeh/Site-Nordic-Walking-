from django.db import models

from .post import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Публикация')
    user_name = models.CharField(max_length=80, verbose_name='Имя пользователя')
    body = models.TextField(max_length=1000, verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        ordering = ('created', )
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий оставлен пользователем {self.user_name} на пост {self.post}.'
