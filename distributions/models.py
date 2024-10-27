from datetime import datetime

from django.db import models

from clients.models import Client
from config.settings import NULLABLE
from letters.models import Letter
from users.models import User
from django.core.exceptions import ValidationError


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
    next_send_datetime = models.CharField(
        max_length=30,
        verbose_name="Дата следующей отправки",
        **NULLABLE,
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
        User, on_delete=models.SET_NULL, verbose_name="Пользователь", **NULLABLE
    )
    clients = models.ManyToManyField(Client, verbose_name="Адресаты")
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, verbose_name="Письмо")
    counter = models.PositiveIntegerField(
        default=0, editable=False, verbose_name="Количество отправлений"
    )

    def clean(self):
        # Проверка, что дата окончания больше даты начала
        if self.last_send_date <= self.first_send_date:
            raise ValidationError("Дата окончания должна быть больше даты начала.")

    def __str__(self):
        return f"Рассылка {self.name}\nДата первой рассылки: {self.first_send_date}\nПериод рассылки {self.period}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ("set_change_status", "can change status is_published"),
        ]


class Attempt(models.Model):
    """
    Модель описывает попытку рассылки
    """

    STATUS_CHOICES = {
        ("done", "выполнена"),
        ("failed", "неудачно"),
    }
    last_attempt = models.DateTimeField(
        verbose_name="Дата и время последней попытки рассылки"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="failed",
        verbose_name="Статус рассылки",
    )
    server_answer = models.TextField(verbose_name="Ответ сервера")
    distributions = models.ForeignKey(
        Distribution, on_delete=models.CASCADE, verbose_name="Рассылка"
    )

    def __str__(self):
        return f"Рассылка {self.distributions.name}. Пользователь: {self.distributions.owner.email}. Дата: {self.last_attempt}. Статус: {self.status}"

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"
        ordering = ("last_attempt",)
