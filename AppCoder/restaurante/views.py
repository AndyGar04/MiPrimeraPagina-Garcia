from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from. import forms, models

from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

# Listado de los metodos presentes.

class PedidoListView(ListView):
    model = models.Pedido
    template_name = 'pedido_list.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = models.Pedido.objects.filter(nombre__icontains=busqueda)
        else:
            queryset = models.Pedido.objects.all()
        return queryset

class GerenteListView(ListView):
    model = models.Gerente
    template_name = 'gerente_list.html'
    context_object_name = 'gerentes'

class EmpleadoListView(ListView):
    model = models.Empleado
    template_name = 'empleado_list.html'
    context_object_name = 'empleados'

# Creacion de los metodos presentes. 

class PedidoCreateView(CreateView):
    model = models.Pedido
    form_class = forms.PedidoForm
    success_url = reverse_lazy("restaurante:pedido_list")
    
class EmpleadoCreateView(CreateView):
    model = models.Empleado
    form_class = forms.EmpleadoForm
    success_url = reverse_lazy("restaurante:empleado_list")
    
class GerenteCreateView(CreateView):
    model = models.Gerente
    form_class = forms.GerenteForm
    success_url = reverse_lazy("restaurante:gerente_list")

# Actualizacion de los metodos presentes.

class PedidoUpdateView(UpdateView):
    model = models.Pedido
    form_class = forms.PedidoForm
    success_url = reverse_lazy("restaurante:pedido_list")
    
class EmpleadoUpdateView(UpdateView):
    model = models.Empleado
    form_class = forms.EmpleadoForm
    success_url = reverse_lazy("restaurante:empleado_list")
    
class GerenteUpdateView(UpdateView):
    model = models.Gerente
    form_class = forms.GerenteForm
    success_url = reverse_lazy("restaurante:gerente_list")

# Eliminar los metodos cargados.

class PedidoDeleteView(DeleteView):
    model = models.Pedido
    template_name = 'restaurante/pedido_confirm_delete.html'
    success_url = reverse_lazy("restaurante:pedido_list")
    
class EmpleadoDeleteView(DeleteView):
    model = models.Empleado
    template_name = 'restaurante/empleado_confirm_delete.html'
    success_url = reverse_lazy("restaurante:empleado_list")
    
class GerenteDeleteView(DeleteView):
    model = models.Gerente
    template_name = 'restaurante/gerente_confirm_delete.html'
    success_url = reverse_lazy("restaurante:gerente_list")

# Detalles de los metodos cargados.

class PedidoDetailView(DetailView):
    model = models.Pedido
    template_name = 'restaurante/pedido_detail.html'
    context_object_name = 'pedido'
    
class EmpleadoDetailView(DetailView):
    model = models.Empleado
    template_name = 'restaurante/empleado_detail.html'
    context_object_name = 'empleado'
    
class GerenteDetailView(DetailView):
    model = models.Gerente
    template_name = 'restaurante/gerente_detail.html'
    context_object_name = 'gerente'

