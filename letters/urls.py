from django.urls import path

from letters.apps import LettersConfig
from letters.views import LettersListView, LettersDetailView, LettersCreateView, LettersUpdateView, LettersDeleteView

app_name = LettersConfig.name

urlpatterns = [
    path('', LettersListView.as_view(), name='letters_list'),
    path('view/<int:pk>/', LettersDetailView.as_view(), name='letters_detail'),
    path('create/', LettersCreateView.as_view(), name='letters_create'),
    path('update/<int:pk>/', LettersUpdateView.as_view(), name='letters_update'),
    path('delete/<int:pk>/', LettersDeleteView.as_view(), name='letters_delete'),
]
