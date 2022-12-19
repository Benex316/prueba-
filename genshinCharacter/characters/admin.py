from django.contrib import admin
from .models import Personaje, Producto, carroCompra, Detalle, Cliente, Venta

# Register your models here.

admin.site.register(Personaje)
admin.site.register(Producto)
admin.site.register(carroCompra)
admin.site.register(Detalle)
admin.site.register(Cliente)
admin.site.register(Venta)
