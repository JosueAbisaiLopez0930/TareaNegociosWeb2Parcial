from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=254)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

class CuentaB(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=30, null=True, blank=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    propietario_cuenta = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Deposito(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    propietario_cuenta = models.ForeignKey(CuentaB, on_delete=models.CASCADE)

class Transaccion(models.Model):

    fecha_Transaccion = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    propietario_cuenta = models.ForeignKey(CuentaB, on_delete=models.CASCADE)
    nombre = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)

class Retiro(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    propietario_cuenta = models.ForeignKey(CuentaB, on_delete=models.CASCADE)