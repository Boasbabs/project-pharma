from django.conf.urls import url
from django.urls import path

from .views import OrderSummaryListView

app_name = 'shopping_cart'

urlpatterns = [
    path("order_summary", OrderSummaryListView.as_view(), name="order_summary"),
]
