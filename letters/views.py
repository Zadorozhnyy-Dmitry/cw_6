from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from letters.forms import LettersForm
from letters.models import Letter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class LettersListView(LoginRequiredMixin, ListView):
    """
    Контроллер отображения списка писем
    """

    model = Letter
    extra_context = {"title": "Письма"}


class LettersDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер отображения одного письма
    """

    model = Letter
    extra_context = {"title": "Письма"}


class LettersCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер создания нового письма
    """

    model = Letter
    form_class = LettersForm
    extra_context = {"title": "Письма"}
    permission_required = 'letters.add_letter'
    success_url = reverse_lazy("letters:letters_list")

    def form_valid(self, form):
        """
        Автоматическая привязка пользователя к письму
        """
        letter = form.save()
        user = self.request.user
        letter.owner = user
        letter.save()
        return super().form_valid(form)


class LettersUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер редактирования письма
    """

    model = Letter
    form_class = LettersForm
    extra_context = {"title": "Письма"}
    permission_required = 'letters.change_letter'
    success_url = reverse_lazy("letters:letters_list")


class LettersDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер удаления письма
    """

    model = Letter
    extra_context = {"title": "Письма"}
    permission_required = 'letters.delete_letter'
    success_url = reverse_lazy("letters:letters_list")
