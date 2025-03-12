from django.shortcuts import render
from .models import Pedido, Gerente, Empleado

def pedido_list(request):
    pedido_list = Pedido.objects.all()
    return render(request, 'restaurante/pedido_list.html', context = {"pedidos": pedido_list})

def gerente_list(request):
    gerente_list = Gerente.objects.all()
    return render(request, 'restaurante/gerente_list.html', context = {"gerentes": gerente_list})

def empleado_list(request):
    empleado_list = Empleado.objects.all()
    return render(request, 'restaurante/empleado_list.html', context = {"empleados": empleado_list})