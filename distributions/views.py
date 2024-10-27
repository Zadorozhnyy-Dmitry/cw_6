from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from distributions.forms import DistributionForm
from distributions.models import Distribution, Attempt
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class DistributionsListView(LoginRequiredMixin, ListView):
    """
    Контролер для списка рассылок
    """

    model = Distribution
    extra_context = {"title": "Рассылки"}


class DistributionsDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для отображения списка адресатов одной рассылки
    """

    model = Distribution
    extra_context = {"title": "Рассылки"}


class DistributionsCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер создания рассылки
    """

    model = Distribution
    form_class = DistributionForm
    extra_context = {"title": "Рассылки"}
    permission_required = 'distributions.add_distribution'
    success_url = reverse_lazy("distributions:distributions_list")

    def form_valid(self, form):
        """
        Автоматическая привязка рассылки к пользователю
        """
        distribution = form.save()
        user = self.request.user
        distribution.owner = user
        distribution.name = (
            distribution.letter.topic
        )  # название рассылки по теме письма
        distribution.save()
        return super().form_valid(form)


class DistributionsUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер изменения рассылки
    """

    model = Distribution
    form_class = DistributionForm
    extra_context = {"title": "Рассылки"}
    permission_required = 'distributions.change_distribution'
    success_url = reverse_lazy("distributions:distributions_list")

    def form_valid(self, form):
        """
        Автоматическое изменение имени при смене письма
        """
        distribution = form.save()
        distribution.name = distribution.letter.topic
        distribution.save()
        return super().form_valid(form)


class DistributionsDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер удаления рассылки
    """

    model = Distribution
    extra_context = {"title": "Рассылки"}
    permission_required = 'distributions.delete_distribution'
    success_url = reverse_lazy("distributions:distributions_list")


class AttemptListView(LoginRequiredMixin, ListView):
    """
    Контроллер попытки рассылки
    """

    model = Attempt
    extra_context = {"title": "Отчеты"}


class AttemptDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер детального описания попытки рассылки
    """

    model = Attempt
    extra_context = {"title": "Отчеты"}
