from django.contrib import admin
from .models import Operacion, Iva, Traslado, Moneda, ImpuestoVario, ConceptoNoGrabado, Otro, Rol, Aeronave, Mecanico, Razon, Operador, Cliente, Piloto, Iva, Categoria, Gasto, Base

class ProductAdmin(admin.ModelAdmin):
    fields = ()

# Register your models here.

admin.site.register(Base)
admin.site.register(Operacion, ProductAdmin)
admin.site.register(Aeronave)
admin.site.register(Piloto)
admin.site.register(Mecanico)
admin.site.register(Razon)
admin.site.register(Operador)
admin.site.register(Traslado)
admin.site.register(Cliente)
admin.site.register(Gasto)
admin.site.register(Moneda)
admin.site.register(Iva)
admin.site.register(ImpuestoVario)
admin.site.register(ConceptoNoGrabado)
admin.site.register(Categoria)
admin.site.register(Otro)
admin.site.register(Rol)
