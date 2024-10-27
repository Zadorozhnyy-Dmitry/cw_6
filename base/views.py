from django.shortcuts import render

from clients.models import Client
from distributions.models import Distribution


def index(request):
    """
    Контроллер отображения главной страницы с образцами
    """
    # считаю кол-во рассылок всего
    total_distributions = Distribution.objects.count()
    # считаю кол-во ежедневных рассылок
    daily_total_distributions = Distribution.objects.filter(period='daily').count()
    daily_created_distributions = Distribution.objects.filter(period='daily', status='created').count()
    daily_launched_distributions = Distribution.objects.filter(period='daily', status='launched').count()
    daily_completed_distributions = Distribution.objects.filter(period='daily', status='completed').count()

    # считаю кол-во еженедельных рассылок
    weekly_total_distributions = Distribution.objects.filter(period='weekly').count()
    weekly_created_distributions = Distribution.objects.filter(period='weekly', status='created').count()
    weekly_launched_distributions = Distribution.objects.filter(period='weekly', status='launched').count()
    weekly_completed_distributions = Distribution.objects.filter(period='weekly', status='completed').count()

    # считаю кол-во ежемесячных рассылок
    monthly_total_distributions = Distribution.objects.filter(period='monthly').count()
    monthly_created_distributions = Distribution.objects.filter(period='monthly', status='created').count()
    monthly_launched_distributions = Distribution.objects.filter(period='monthly', status='launched').count()
    monthly_completed_distributions = Distribution.objects.filter(period='monthly', status='completed').count()

    # кол-во уникальных клиентов
    unique_clients = Client.objects.values('client_email').distinct().count()

    context = {
        'title': 'Главная',
        'total': total_distributions,

        'daily_total': daily_total_distributions,
        'daily_created': daily_created_distributions,
        'daily_launched': daily_launched_distributions,
        'daily_completed': daily_completed_distributions,

        'weekly_total': weekly_total_distributions,
        'weekly_created': weekly_created_distributions,
        'weekly_launched': weekly_launched_distributions,
        'weekly_completed': weekly_completed_distributions,

        'monthly_total': monthly_total_distributions,
        'monthly_created': monthly_created_distributions,
        'monthly_launched': monthly_launched_distributions,
        'monthly_completed': monthly_completed_distributions,

        'unique_clients': unique_clients
    }
    return render(request, "base/examples_list.html", context)


def clients_list_examples(request):
    """
    Контроллер отображения образца со списком клиентов
    """
    context = {'title': 'Главная', }
    return render(request, "base/examples_clients.html", context)
