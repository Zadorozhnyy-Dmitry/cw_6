from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from clients.models import Client


class ClientsListView(ListView):
    """
    Контроллер для отображения списка клиентов
    """
    model = Client
    extra_context = {'title': 'Клиенты'}


class ClientsCreateView(CreateView):
    """
    Контроллер для создания клиента
    """
    model = Client
    fields = (
        "name",
        "client_email",
        "comments",
    )
    extra_context = {'title': 'Клиенты'}
    success_url = reverse_lazy("clients:clients_list")

    def form_valid(self, form):
        """
        Автоматическая привязка клиента к пользователю
        """
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientsUpdateView(UpdateView):
    """
    Контроллер для изменения клиента
    """

    model = Client
    fields = (
        "name",
        "client_email",
        "comments",
    )
    extra_context = {'title': 'Клиенты'}
    success_url = reverse_lazy("clients:clients_list")


class ClientsDeleteView(DeleteView):
    """
    Контроллер для удаления клиента из списка
    """

    model = Client
    extra_context = {'title': 'Клиенты'}
    success_url = reverse_lazy("clients:clients_list")
