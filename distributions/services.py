import smtplib
from datetime import timedelta, datetime

from distributions.models import Distribution, Attempt
from django.core.mail import send_mail
from config import settings
from django.utils import timezone


def start_time_to_str(distribution: Distribution):
    """
    Функция преобразует два поля начала рассылки в одну строковую форму
    """
    str_start_send = (distribution.first_send_date.strftime('%Y-%m-%d') +
                      distribution.first_send_time.strftime(' %H:%M:%S'))

    return str_start_send


def stop_time_to_str(distribution: Distribution):
    """
    Функция преобразует два поля конца рассылки в одну строковую форму
    при ее отсутствии задаю плюс год
    """
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

    return str_stop_send


def next_time_to_str(distribution: Distribution):
    """
    Функция рассчитывает дату следующей рассылки с учетом текущей даты
    """
    # переменная для определения атрибута timedelta
    delta_time_dict = {'daily': 1, 'weekly': 7, 'monthly': 30, }
    # текущая дата
    str_now = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

    next_date = distribution.first_send_date + timedelta(days=delta_time_dict[distribution.period])
    str_next_date = (next_date.strftime('%Y-%m-%d') +
                     distribution.first_send_time.strftime(' %H:%M:%S'))
    while str_next_date < str_now:
        next_date += timedelta(days=delta_time_dict[distribution.period])
        str_next_date = (next_date.strftime('%Y-%m-%d') +
                         distribution.first_send_time.strftime(' %H:%M:%S'))

    return str_next_date


def send_email(distribution: Distribution):
    """
    Функция рассылки почты
    """
    # Определяю список клиентов
    clients_list = [client.client_email for client in distribution.clients.all()]

    try:
        # функция отправки
        send_mail(
            distribution.letter.topic,
            distribution.letter.body,
            settings.EMAIL_HOST_USER,
            clients_list,
            fail_silently=False,
        )
        # запись отчета об успешной попытке рассылки
        Attempt.objects.create(
            last_attempt=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            status='done',
            server_answer='Рассылка выполнена',
            distributions=distribution,

        )
    except smtplib.SMTPException as e:
        # При ошибке почтовика получаем ответ сервера - ошибка, которая записывается в е
        Attempt.objects.create(
            last_attempt=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            status='failed',
            server_answer=str(e),
            distributions=distribution,

        )
