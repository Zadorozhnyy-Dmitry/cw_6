from django.urls import path

from distributions.apps import DistributionsConfig
from distributions.views import DistributionsListView, DistributionsDetailView, DistributionsCreateView, \
    DistributionsUpdateView, DistributionsDeleteView

app_name = DistributionsConfig.name

urlpatterns = [
    path("", DistributionsListView.as_view(), name="distributions_list"),
    path("detail/<int:pk>/", DistributionsDetailView.as_view(), name="distributions_detail"),
    path("update/<int:pk>/", DistributionsUpdateView.as_view(), name="distributions_edit"),
    path("delete/<int:pk>/", DistributionsDeleteView.as_view(), name="distributions_delete"),
    path("create/", DistributionsCreateView.as_view(), name="distributions_create"),
]
