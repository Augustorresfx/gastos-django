from django.contrib import admin
from .models import Operacion, Aeronave, Mecanico, Razon, Operador, Cliente, Piloto, Impuesto, Categoria, Gasto


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Operacion, ProductAdmin)
admin.site.register(Aeronave)
admin.site.register(Piloto)
admin.site.register(Mecanico)
admin.site.register(Razon)
admin.site.register(Operador)
admin.site.register(Cliente)
admin.site.register(Gasto)
admin.site.register(Impuesto)
admin.site.register(Categoria)
