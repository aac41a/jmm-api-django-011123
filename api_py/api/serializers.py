# api/serializers.py
from rest_framework import serializers
from .models import Departamento, Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    empleados = EmpleadoSerializer(many=True, read_only=True)

    class Meta:
        model = Departamento
        fields = '__all__'