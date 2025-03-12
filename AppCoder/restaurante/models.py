from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Gerente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='gerente')
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(validators=[MinValueValidator(16)])
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(validators=[MinValueValidator(16)])
    observaciones = models.TextField(blank=True, null=True)
    horario_de_trabajo = models.TextField()

    def __str__(self):
        return self.nombre     

class Pedido(models.Model):
    class Estado(models.TextChoices):
        ENTREGADO = "E", "Entregado"
        NO_ENTREGADO= "N" , "No entregado"
    nombre = models.TextField()
    horario_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.NO_ENTREGADO)    
    empleado_a_cargo = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre