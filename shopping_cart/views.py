from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from drugs.models import Drug
from frontend.decorators import retailer_required


@method_decorator([login_required, retailer_required], name='dispatch')
class OrderSummaryListView(ListView):
    model = Drug
    template_name = "shopping_cart/order_summary.html"
    paginate_by = 10