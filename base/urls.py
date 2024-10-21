from django.urls import path

from base.apps import BaseConfig
from base.views import index, clients_list_examples

app_name = BaseConfig.name

urlpatterns = [
    path('', index, name='examples_list'),
    path('examples-clients/', clients_list_examples, name='examples_clients'),
]
