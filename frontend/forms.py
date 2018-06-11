from django import forms
# from allauth.account.forms import SignupForm

from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.db.transaction import commit

from frontend.models import User, Retailer, Wholesaler


class WholesalerSignupForm(UserCreationForm):
    wholesaler_name = forms.CharField(label='Your Business Name', max_length=150, required=True)
    facility_reg_number = forms.IntegerField()
    phone_number = forms.CharField(max_length=15, help_text='Required. Enter a valid phone number.')
    location = forms.CharField(label='Your location', help_text='Required. Inform a valid address.', max_length=225)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        # Ensure you call the parent classes save.
        # .save() returns a User object.
        user = super().save(commit=False)
        user.is_wholesaler = True
        user.save()
        Wholesaler.objects.create(user=user,
                                  wholesaler_name=self.cleaned_data.get("wholesaler_name"),
                                  facility_reg_number=self.cleaned_data.get("facility_reg_number"),
                                  phone_number=self.cleaned_data.get("phone_number"),
                                  location=self.cleaned_data.get("location"),
                                  )
        return user

    def clean(self):
        cleaned_data = super(WholesalerSignupForm, self).clean()


class RetailerSignupForm(UserCreationForm):
    retailer_name = forms.CharField(label='Your Business Name', max_length=150)
    facility_reg_number = forms.IntegerField()
    phone_number = forms.CharField(max_length=15)
    location = forms.CharField(label='Your location', max_length=225)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_retailer = True
        user.save()
        Retailer.objects.create(user=user,
                                retailer_name=self.cleaned_data.get("retailer_name"),
                                facility_reg_number=self.cleaned_data.get("facility_reg_number"),
                                phone_number=self.cleaned_data.get("phone_number"),
                                location=self.cleaned_data.get("location"),
                                )

        return user

    def clean(self):
        cleaned_data = super(RetailerSignupForm, self).clean()
