from django.contrib import admin
from .models import Product, Category, Mechanic, Reason, Operator, Client


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Mechanic)
admin.site.register(Reason)
admin.site.register(Operator)
admin.site.register(Client)
