from django.db import models
from django.contrib.auth.models import User

class Gerente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    observaciones = models.TextField()

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    observaciones = models.TextField()
    horario_de_trabajo = models.TextField()

    def __str__(self):
        return self.nombre     

class Pedidos(models.Model):
    class Estado(models.TextChoices):
        ENTREGADO = "E", "Entregado"
        NO_ENTREGADO= "N" , "No entregado"
    plato = models.TextField()
    horario_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.BORRADOR)    
    empleado_a_cargo = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.plato