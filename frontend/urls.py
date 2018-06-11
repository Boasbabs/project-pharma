from django.urls import path, include

from .views import landing

app_name = "frontend"
urlpatterns = [
    path("", landing.index, name="index"),
    # path("results", results, name="results")
]


