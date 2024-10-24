from django.urls import path

from letters.apps import LettersConfig
from letters.views import LettersListView, LettersDetailView, LettersCreateView, LettersUpdateView, LettersDeleteView

app_name = LettersConfig.name

urlpatterns = [
    path('', LettersListView.as_view(), name='letters_list'),  # перечень писем
    path('view/<int:pk>/', LettersDetailView.as_view(), name='letters_detail'),  # просмотр одного письма
    path('create/', LettersCreateView.as_view(), name='letters_create'),  # создать письмо
    path('update/<int:pk>/', LettersUpdateView.as_view(), name='letters_update'),  # изменить письмо
    path('delete/<int:pk>/', LettersDeleteView.as_view(), name='letters_delete'),  # удалить письмо
]
