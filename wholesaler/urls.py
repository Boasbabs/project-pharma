from django.urls import path

from . import views


app_name = "wholesaler"
urlpatterns = [
    path("", views.WholesalerHomeDetailView.as_view(), name="home"),
    path("detail", views.DriverRequestDetailView.as_view(), name="order_detail"),
    path("list", views.DriverRequestListView.as_view(), name="order_list"),
]
