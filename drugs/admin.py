from django.contrib import admin

from drugs.models import Drug


class DrugAdmin(admin.ModelAdmin):
    list_display = ("generic_name", "brand_name", "pack_size", "price", "date_added")
    list_filter = ("generic_name", "brand_name", "date_added")
    search_fields = ("title", "body")
    ordering = ["generic_name", "brand_name"]


admin.site.register(Drug, DrugAdmin)
