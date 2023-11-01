# api/views.py
from rest_framework import viewsets
from .models import Departamento, Empleado
from .serializers import DepartamentoSerializer, EmpleadoSerializer

class DepartamentoList(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class EmpleadoList(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


