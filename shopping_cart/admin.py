from django.contrib import admin
from shopping_cart.models import Order, OrderItem


admin.site.register(Order)
admin.site.register(OrderItem)
