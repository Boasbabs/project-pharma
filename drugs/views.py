from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from drugs.models import Drug
from frontend.decorators import retailer_required


# @method_decorator([login_required], name='dispatch')
class DrugListView(ListView):
    model = Drug
    template_name = "drugs/drugslist.html"
    paginate_by = 10