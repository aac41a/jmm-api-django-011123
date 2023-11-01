# api/models.py
from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, related_name='empleados', on_delete=models.CASCADE)

