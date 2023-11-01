# api/urls.py
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'empleados',views.EmpleadoList)
router.register(r'departamentos', views.DepartamentoList)

urlpatterns = [
    path('', include(router.urls))
]
