from django.db import models

from config.settings import NULLABLE
from users.models import User


class Letter(models.Model):
    """
    Модель описывает письмо клиенту
    """

    topic = models.CharField(
        max_length=100,
        verbose_name="Тема письма",
        help_text="Укажите тему письма",
    )
    body = models.TextField(verbose_name="Текст письма", help_text="Укажите содержание письма")

    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Пользователь", **NULLABLE
    )

    def __str__(self):
        return f"{self.topic}"

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"
