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


class LettersCreateView(CreateView):
    """
    Контроллер создания нового письма
    """
    model = Letter
    fields = ('topic', 'body',)
    success_url = reverse_lazy('letters:letters_list')

    def form_valid(self, form):
        """
        Автоматическая привязка пользователя к письму
        """
        letter = form.save()
        user = self.request.user
        letter.owner = user
        letter.save()
        return super().form_valid(form)


class LettersUpdateView(UpdateView):
    """
    Контроллер редактирования письма
    """
    model = Letter
    fields = ('topic', 'body',)
    success_url = reverse_lazy('letters:letters_list')


class LettersDeleteView(DeleteView):
    """
    Контроллер удаления письма
    """
    model = Letter
    success_url = reverse_lazy("letters:letters_list")
