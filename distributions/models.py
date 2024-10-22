from datetime import datetime

from django.db import models

from clients.models import Client
from config.settings import NULLABLE
from letters.models import Letter
from users.models import User


class Distribution(models.Model):
    """
    Модель описывает рассылку
    """

    PERIOD_CHOICES = {
        ("daily", "ежедневно"),
        ("weekly", "еженедельно"),
        ("monthly", "ежемесячно"),
    }
    STATUS_CHOICES = {
        ("created", "создана"),
        ("launched", "запущена"),
        ("completed", "завершена"),
    }
    name = models.CharField(
        max_length=150,
        verbose_name="Название",
    )
    first_send_date = models.DateField(
        default=datetime.now,
        verbose_name="Дата первой отправки",
    )
    first_send_time = models.TimeField(
        default=datetime.now,
        verbose_name="Время первой отправки",
    )
    last_send_date = models.DateField(
        verbose_name="Дата последней отправки",
        **NULLABLE,
    )
    last_send_time = models.TimeField(
        verbose_name="Время последней отправки",
        **NULLABLE,
    )
    period = models.CharField(
        max_length=20,
        choices=PERIOD_CHOICES,
        default="ежедневно",
        verbose_name="Периодичность рассылки",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="created",
        verbose_name="Статус рассылки",
    )

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Заказчик", **NULLABLE
    )
    clients = models.ManyToManyField(Client, verbose_name="Адресаты")
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, verbose_name='Письмо')

    def __str__(self):
        return f"Рассылка {self.name}\nДата первой рассылки: {self.first_send_date}\nПериод рассылки {self.period}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
