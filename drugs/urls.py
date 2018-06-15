from django.conf.urls import url
from django.urls import path

from .views import DrugListView

app_name = 'drugs'

urlpatterns = [
    path("list", DrugListView.as_view(), name="drug_list"),
]
