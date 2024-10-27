from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from clients.forms import ClientsForm
from clients.models import Client
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ClientsListView(LoginRequiredMixin, ListView):
    """
    Контроллер для отображения списка клиентов
    """

    model = Client
    extra_context = {"title": "Клиенты"}


class ClientsCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания клиента
    """

    model = Client
    form_class = ClientsForm
    extra_context = {"title": "Клиенты"}
    permission_required = 'clients.add_client'
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


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для изменения клиента
    """

    model = Client
    form_class = ClientsForm
    extra_context = {"title": "Клиенты"}
    permission_required = 'clients.change_client'
    success_url = reverse_lazy("clients:clients_list")


class ClientsDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления клиента из списка
    """

    model = Client
    extra_context = {"title": "Клиенты"}
    permission_required = 'clients.delete_client'
    success_url = reverse_lazy("clients:clients_list")
