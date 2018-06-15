from django.contrib.auth.models import AbstractUser
from django.db import models
from drugs.models import Drug

# Reference: https://simpleisbetterthancomplex.com
# /tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html


class User(AbstractUser):
    is_retailer = models.BooleanField(default=False)
    is_wholesaler = models.BooleanField(default=False)


class Retailer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="retailer")
    retailer_name = models.CharField(max_length=150)
    facility_reg_number = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=225)

    def __str__(self):
        return self.retailer_name


class Wholesaler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="wholesaler")
    wholesaler_name = models.CharField(max_length=150)
    facility_reg_number = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=225)

    def __str__(self):
        return self.wholesaler_name