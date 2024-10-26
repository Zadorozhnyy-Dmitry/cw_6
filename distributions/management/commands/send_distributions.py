from django.core.management import BaseCommand

from distributions.models import Distribution

from datetime import datetime, timedelta


class Command(BaseCommand):
    """
    Команда для организации рассылок
    """

    def handle(self, *args, **options):
        # переменная для определения атрибута timedelta
        delta_time_dict = {'daily': 1, 'weekly': 7, 'monthly': 30, }
        # прохожу по рассылкам
        for distribution in Distribution.objects.all():
            # если статус "завершена", то пропуск рассылки
            if distribution.status == 'completed':
                continue
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
                print('start_app')
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
