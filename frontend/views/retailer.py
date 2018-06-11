from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView

from ..models import User, Retailer
from ..forms import RetailerSignupForm


class RetailerSignUpView(CreateView):
    model = User
    form_class = RetailerSignupForm
    template_name = "registration/user_signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "retailer"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("frontend:index")
