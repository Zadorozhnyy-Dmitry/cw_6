from django.core.mail import send_mail

from clients.models import Client
from distributions.models import Distribution


def send_distributions_mail():
    """
    Функция отправки рассылок
    """
    # Получаю список всех рассылок
    all_email = []
    for client in Client.objects.all():
        all_email.append(str(client.email))

    print(all_email)


if __name__ == '__main__':
    send_distributions_mail()
