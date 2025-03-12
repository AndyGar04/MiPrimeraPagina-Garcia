from django.contrib import admin
from .models import Gerente, Empleado, Pedido

@admin.register(Gerente)
class GerenteAdmin(admin.ModelAdmin):
    list_display = ["user", "nombre", "edad", "observaciones"]
    list_filter = ["nombre", "edad"]
    raw_id_fields = ["user"] 

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "horario_pedido", "estado", "empleado_a_cargo"]
    list_filter = ["estado", "horario_pedido"]
    raw_id_fields = ["empleado_a_cargo"]
    ordering = ["horario_pedido"]

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "edad", "observaciones", "horario_de_trabajo"]
    list_filter = ["nombre", "edad"]
    #raw_id_fields = ["user"]