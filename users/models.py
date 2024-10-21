from django.db import models
from django.contrib.auth.models import AbstractUser

from config.settings import NULLABLE


class User(AbstractUser):
    """
    Модель для пользователей
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")

    token = models.CharField(max_length=100, verbose_name="токен", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
