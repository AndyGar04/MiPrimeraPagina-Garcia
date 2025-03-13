from django.urls import path
from . import views

app_name = "restaurante"

urlpatterns = [
    path("gerente_list/", views.gerente_list, name="gerente_list"),
    path("pedido_list/", views.pedido_list, name="pedido_list"),
    path("empleado_list/", views.empleado_list, name="empleado_list"),
]