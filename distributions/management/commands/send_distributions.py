from django.core.management import BaseCommand

from distributions.models import Distribution

from datetime import datetime, timedelta
from django.core.mail import send_mail
from config import settings


class Command(BaseCommand):
    """
    Команда для организации рассылок
    """

    def handle(self, *args, **options):
        # переменная для определения атрибута timedelta
        delta_time_dict = {'daily': 1, 'weekly': 7, 'monthly': 30, }
        # прохожу по рассылкам, если статус "завершена", то пропуск рассылки
        for distribution in Distribution.objects.exclude(status='completed'):
            # конвертирую даты в строки для их сравнения
            # конвертирую текущую дату и время в строку
            str_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # конвертирую дату и время первой отправки в строку
            str_start_send = (distribution.first_send_date.strftime('%Y-%m-%d') +
                              distribution.first_send_time.strftime(' %H:%M:%S'))

            # конвертирую дату и время последней отправки в строку, при ее отсутствии задаю плюс год
            if distribution.last_send_date:
                if distribution.last_send_time:
                    str_stop_send = (distribution.last_send_date.strftime('%Y-%m-%d') +
                                     distribution.last_send_time.strftime(' %H:%M:%S'))
                else:
                    str_stop_send = (distribution.last_send_date.strftime('%Y-%m-%d') +
                                     ' 00:00:00')
            else:
                stop_date = distribution.first_send_date + timedelta(days=365)
                str_stop_send = (stop_date.strftime('%Y-%m-%d') + ' 00:00:00')

            # если рассылок не было, то оцениваю дату первой рассылки
            # если рассылки были оцениваю дату следующей отправки
            if (distribution.counter == 0 and str_start_send < str_now or
                    distribution.counter > 0 and distribution.next_send_datetime < str_now):

                # запускаю рассылку
                self.send_email(distribution)

                # увеличиваю счетчик
                distribution.counter += 1

                # определяю дату следующей отправки и конвертирую в строку
                next_date = distribution.first_send_date + timedelta(days=delta_time_dict[distribution.period])
                str_next_date = (next_date.strftime('%Y-%m-%d') +
                                 distribution.first_send_time.strftime(' %H:%M:%S'))
                while str_next_date < str_now:
                    next_date += timedelta(days=delta_time_dict[distribution.period])
                    str_next_date = (next_date.strftime('%Y-%m-%d') +
                                     distribution.first_send_time.strftime(' %H:%M:%S'))
                distribution.next_send_datetime = str_next_date

                # меняю статус
                if str_next_date > str_stop_send:
                    distribution.status = 'completed'
                else:
                    distribution.status = 'launched'

                # сохраняю поля, которые менял
                distribution.save(update_fields=["status", "next_send_datetime", "counter", ])

    @staticmethod
    def send_email(distribution):
        """
        Функция рассылки почты
        """
        # Определяю список клиентов
        clients_list = [client.client_email for client in distribution.clients.all()]

        # функция отправки
        send_mail(
            distribution.letter.topic,
            distribution.letter.body,
            settings.EMAIL_HOST_USER,
            clients_list,
        )
