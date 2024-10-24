from django.shortcuts import render


def index(request):
    """
    Контроллер отображения главной страницы с образцами
    """
    context = {'title': 'Главная', }
    return render(request, "base/examples_list.html", context)


def clients_list_examples(request):
    """
    Контроллер отображения образца со списком клиентов
    """
    context = {'title': 'Главная', }
    return render(request, "base/examples_clients.html", context)
