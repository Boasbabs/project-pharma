from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView

from ..models import User, Wholesaler
from ..forms import WholesalerSignupForm


class WholesalerSignUpView(CreateView):
    model = User
    form_class = WholesalerSignupForm
    template_name = "registration/user_signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "wholesaler"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("frontend:index")