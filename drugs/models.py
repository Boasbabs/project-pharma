from django.db import models


class Drug(models.Model):
    generic_name = models.CharField(max_length=70)
    brand_name = models.CharField(max_length=70)
    physical_form = models.CharField(max_length=70)
    pack_size = models.IntegerField()
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)

    # META CLASS
    class Meta:
        verbose_name = 'drug'
        verbose_name_plural = 'drugs'

    # TO STRING METHOD
    def __str__(self):
        return "Generic Drug Name: {0}, Brand Name: {1}".format(self.generic_name, self.brand_name)


