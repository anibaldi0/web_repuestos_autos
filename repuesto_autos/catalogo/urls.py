# catalogo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_catalogo_repuestos, name='catalogo_repuestos'),  # La ruta raíz para 'catalogo'
]


