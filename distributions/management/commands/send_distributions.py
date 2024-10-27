import logging

from django.core.management import BaseCommand

from distributions.models import Distribution

from distributions.services import (
    start_time_to_str,
    stop_time_to_str,
    next_time_to_str,
    send_email,
)
from django.utils import timezone


class Command(BaseCommand):
    """
    Команда для организации рассылок
    """

    def handle(self, *args, **options):
        # прохожу по рассылкам, если статус "завершена", то пропуск рассылки
        for distribution in Distribution.objects.exclude(status="completed"):
            # конвертирую даты в строки для их сравнения
            # конвертирую текущую дату и время в строку
            str_now = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

            # конвертирую дату и время первой отправки в строку
            str_start_send = start_time_to_str(distribution)

            # конвертирую дату и время последней отправки в строку
            str_stop_send = stop_time_to_str(distribution)

            # если рассылок не было, то оцениваю дату первой рассылки
            # если рассылки были оцениваю дату следующей отправки
            if (
                distribution.counter == 0
                and str_start_send < str_now
                or distribution.counter > 0
                and distribution.next_send_datetime < str_now
            ):

                # запускаю рассылку
                send_email(distribution)

                # увеличиваю счетчик
                distribution.counter += 1

                # определяю дату следующей отправки и конвертирую в строку
                str_next_date = next_time_to_str(distribution)
                distribution.next_send_datetime = str_next_date

                # меняю статус
                if str_next_date > str_stop_send:
                    distribution.status = "completed"
                else:
                    distribution.status = "launched"

                # сохраняю поля, которые менял
                distribution.save(
                    update_fields=[
                        "status",
                        "next_send_datetime",
                        "counter",
                    ]
                )
