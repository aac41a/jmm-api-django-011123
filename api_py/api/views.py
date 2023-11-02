# api/views.py
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Departamento, Empleado
from .serializers import DepartamentoSerializer, EmpleadoSerializer
from rest_framework.permissions import IsAuthenticated

class DepartamentoList(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class EmpleadoList(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
