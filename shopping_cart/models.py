from django.db import models
from frontend.models import Retailer
from drugs.models import Drug


class OrderItem(models.Model):
    drug = models.OneToOneField(Drug, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return "Item: brand {}, generic name {}".format(self.drug.brand_name, self.drug.brand_name)


class Order(models.Model):
    invoice_number = models.CharField(max_length=25)
    retailer = models.ForeignKey(Retailer, related_name="retailer_orders", on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(OrderItem)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.drug.price for item in self.items.all()])

    def __str__(self):
        return '{0}'.format(self.invoice_number)