from django.urls import path
from django.contrib.auth.decorators import login_required 
from . import views

app_name = "restaurante"

urlpatterns = [
    #Vistas
    path("gerente/", login_required(views.GerenteListView.as_view()), name="gerente_list"),
    path("empleado/", login_required(views.EmpleadoListView.as_view()), name="empleado_list"),
    path('pedido/', login_required(views.PedidoListView.as_view()), name='pedido_list'),
    #Detalles
    path('pedido_detail/<int:pk>/', login_required(views.PedidoDetailView.as_view()), name='pedido_detail'),
    path('gerente_detail/<int:pk>/', login_required(views.GerenteDetailView.as_view()), name='gerente_detail'),
    path('empleado_detail/<int:pk>/', login_required(views.EmpleadoDetailView.as_view()), name='empleado_detail'),
    #Crear
    path('pedido_create/', login_required(views.PedidoCreateView.as_view()), name='pedido_form'),
    path('gerente_create/', login_required(views.GerenteCreateView.as_view()), name='gerente_form'),
    path('empleado_create/', login_required(views.EmpleadoCreateView.as_view()), name='empleado_form'),
    #Actualizar
    path('pedido_update/<int:pk>/', login_required(views.PedidoUpdateView.as_view()), name='pedido_form'),
    path('gerente_update/<int:pk>/', login_required(views.GerenteUpdateView.as_view()), name='gerente_form'),
    path('empleado_update/<int:pk>/', login_required(views.EmpleadoUpdateView.as_view()), name='empleado_form'),
    #Eliminar
    path('pedido_delete/<int:pk>/', login_required(views.PedidoDeleteView.as_view()), name='pedido_confirm_delete'),
    path('gerente_delete/<int:pk>/', login_required(views.GerenteDeleteView.as_view()), name='gerente_confirm_delete'),
    path('empleado_delete/<int:pk>/', login_required(views.EmpleadoDeleteView.as_view()), name='empleado_confirm_delete'),
]