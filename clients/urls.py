from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientsListView, ClientsCreateView, ClientsUpdateView, ClientsDeleteView

app_name = ClientsConfig.name

urlpatterns = [
    path("", ClientsListView.as_view(), name="clients_list"),  # просмотр списка клиентов
    path("create/", ClientsCreateView.as_view(), name="clients_create"),  # создать клиента
    path("update/<int:pk>/", ClientsUpdateView.as_view(), name="clients_update"),  # редактировать запись клиента
    path("delete/<int:pk>/", ClientsDeleteView.as_view(), name="clients_delete"),  # удалить клиента
]
