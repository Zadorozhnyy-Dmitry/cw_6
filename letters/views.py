from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from letters.models import Letter


class LettersListView(ListView):
    """
    Контроллер отображения списка писем
    """
    model = Letter


class LettersDetailView(DetailView):
    """
    Контроллер отображения одного письма
    """
    model = Letter


class LetterCreateView(CreateView):
    """
    Контроллер создания нового письма
    """
    pass


