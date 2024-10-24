from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from distributions.models import Distribution, Attempt


class DistributionsListView(ListView):
    """
    Контролер для списка рассылок
    """

    model = Distribution
    extra_context = {'title': 'Рассылки'}


class DistributionsDetailView(DetailView):
    """
    Контроллер для отображения списка адресатов одной рассылки
    """

    model = Distribution
    extra_context = {'title': 'Рассылки'}


class DistributionsCreateView(CreateView):
    """
    Контроллер создания рассылки
    """

    model = Distribution
    fields = (
        "first_send_date", "first_send_time", "last_send_date", "last_send_time", "period", "clients", "letter",
    )
    extra_context = {'title': 'Рассылки'}
    success_url = reverse_lazy("distributions:distributions_list")

    def form_valid(self, form):
        """
        Автоматическая привязка рассылки к пользователю
        """
        distribution = form.save()
        user = self.request.user
        distribution.owner = user
        distribution.name = distribution.letter.topic  # название рассылки по теме письма
        distribution.save()
        return super().form_valid(form)


class DistributionsUpdateView(UpdateView):
    """
    Контроллер изменения рассылки
    """

    model = Distribution
    fields = (
        "first_send_date", "first_send_time", "last_send_date", "last_send_time", "period", "clients", "letter",
    )
    extra_context = {'title': 'Рассылки'}
    success_url = reverse_lazy("distributions:distributions_list")

    def form_valid(self, form):
        """
        Автоматическое изменение имени при смене письма
        """
        distribution = form.save()
        distribution.name = distribution.letter.topic
        distribution.save()
        return super().form_valid(form)


class DistributionsDeleteView(DeleteView):
    """
    Контроллер удаления рассылки
    """

    model = Distribution
    extra_context = {'title': 'Рассылки'}
    success_url = reverse_lazy("distributions:distributions_list")


class AttemptListView(ListView):
    """
    Контроллер попытки рассылки
    """
    model = Attempt
    extra_context = {'title': 'Отчеты'}


class AttemptDetailView(DetailView):
    """
    Контроллер детального описания попытки рассылки
    """
    model = Attempt
    extra_context = {'title': 'Отчеты'}
