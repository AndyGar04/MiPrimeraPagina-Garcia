from django import forms
from .models import Pedido, Empleado, Gerente

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['horario_pedido']
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["nombre", "edad", "observaciones", "horario_de_trabajo"]
        
class GerenteForm(forms.ModelForm):
    class Meta:
        model = Gerente
        fields = ["user", "nombre", "edad", "observaciones"]