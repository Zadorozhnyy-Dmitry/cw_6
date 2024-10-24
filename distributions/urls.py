from django.urls import path

from distributions.apps import DistributionsConfig
from distributions.views import DistributionsListView, DistributionsDetailView, DistributionsCreateView, \
    DistributionsUpdateView, DistributionsDeleteView, AttemptListView, AttemptDetailView

app_name = DistributionsConfig.name

urlpatterns = [
    path("", DistributionsListView.as_view(), name="distributions_list"),  # список рассылок
    path("detail/<int:pk>/", DistributionsDetailView.as_view(), name="distributions_detail"),  # просмотр одной рассылки
    path("update/<int:pk>/", DistributionsUpdateView.as_view(), name="distributions_update"),  # редактирование рассылки
    path("delete/<int:pk>/", DistributionsDeleteView.as_view(), name="distributions_delete"),  # удаление рассылки
    path("create/", DistributionsCreateView.as_view(), name="distributions_create"),  # создание рассылки

    path('attempt/', AttemptListView.as_view(), name='attempt_list'),  # список попыток рассылки
    path('attempt/<int:pk>', AttemptDetailView.as_view(), name='attempt_detail'),  # просмотр одной попытки
]
