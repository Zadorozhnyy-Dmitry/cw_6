# Generated by Django 4.2 on 2024-10-24 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("distributions", "0005_alter_distribution_period"),
    ]

    operations = [
        migrations.AlterField(
            model_name="distribution",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AlterField(
            model_name="distribution",
            name="status",
            field=models.CharField(
                choices=[
                    ("launched", "запущена"),
                    ("completed", "завершена"),
                    ("created", "создана"),
                ],
                default="created",
                max_length=20,
                verbose_name="Статус рассылки",
            ),
        ),
        migrations.CreateModel(
            name="Attempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_attempt",
                    models.DateField(
                        verbose_name="Дата и время последней попытки рассылки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("done", "выполнена"), ("failed", "неудачно")],
                        default="failed",
                        max_length=20,
                        verbose_name="Статус рассылки",
                    ),
                ),
                ("server_answer", models.TextField(verbose_name="Ответ сервера")),
                (
                    "distributions",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="distributions.distribution",
                        verbose_name="Рассылка",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "попытка рассылки",
                "verbose_name_plural": "попытки рассылки",
                "ordering": ("status",),
            },
        ),
    ]