from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render
from django.urls import reverse_lazy

from distributions.models import Distribution


class DistributionsListView(ListView):
    """
    Контролер для списка рассылок
    """

    model = Distribution


class DistributionsDetailView(DetailView):
    """
    Контроллер для отображения списка адресатов одной рассылки
    """

    model = Distribution


class DistributionsCreateView(CreateView):
    """
    Контроллер создания рассылки
    """

    model = Distribution
    fields = (
        "name", "first_send_date", "first_send_time", "last_send_date", "last_send_time", "period", "clients", "letter",
    )
    success_url = reverse_lazy("distributions:distributions_list")

    def form_valid(self, form):
        """
        Автоматическая привязка рассылки к пользователю
        """
        distribution = form.save()
        user = self.request.user
        distribution.owner = user
        distribution.save()
        return super().form_valid(form)


class DistributionsUpdateView(UpdateView):
    """
    Контроллер изменения рассылки
    """

    model = Distribution
    fields = (
        "name", "first_send_date", "first_send_time", "last_send_date", "last_send_time", "period", "clients", "letter",
    )
    success_url = reverse_lazy("distributions:distributions_list")


class DistributionsDeleteView(DeleteView):
    """
    Контроллер удаления рассылки
    """

    model = Distribution
    success_url = reverse_lazy("distributions:distributions_list")
