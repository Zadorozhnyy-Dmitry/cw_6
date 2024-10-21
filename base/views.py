from django.shortcuts import render


def index(request):
    """
    Контроллер отображения главной страницы с образцами
    """
    return render(request, "base/examples_list.html")


def clients_list_examples(request):
    """
    Контроллер отображения образца со списком клиентов
    """
    return render(request, "base/examples_clients.html")
