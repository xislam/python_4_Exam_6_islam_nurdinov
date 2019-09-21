from django.db import models

status_choices = [("active", "Активно"), ("blocked", "Заблокировано")]


class Guestbook(models.Model):
    post_author_name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя Автора')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name='Email')
    date = models.DateField(max_length=3000, null=True, blank=True, verbose_name='Дата')
    creation_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')
    change_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Дата_изменения')
    status = models.CharField(max_length=20, verbose_name='Тема', default=status_choices[0][0], choices=status_choices)

    def __str__(self):
        return self.post_author_name
