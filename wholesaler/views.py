from django.shortcuts import render
from django.views.generic import TemplateView


class WholesalerHomeDetailView(TemplateView):
    template_name = "wholesaler/dashboard.html"


class DriverRequestDetailView(TemplateView):
    template_name = "wholesaler/order_detail.html"


class DriverRequestListView(TemplateView):
    template_name = "wholesaler/order_list.html"

