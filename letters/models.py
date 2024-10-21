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
        help_text="Укажите название рассылки",
    )
    body = models.TextField(verbose_name="Тело письма")

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE
    )

    def __str__(self):
        return f"{self.topic}"

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"
