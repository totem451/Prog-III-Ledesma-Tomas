# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render


def index(request):
	clasificaciones = Clasificacion.objects.all()
	return render(request, 'index.html', {'todas_las_clasificaciones':clasificaciones})

def ver_clasificaciones(request, clasificacion_id):
	clasificacion_elegida = Clasificacion.objects.get(id=clasificacion_id)
	producto = Producto.objects.filter(clasificacion=clasificacion_elegida)
	return render(request, 'producto.html', {'mi_clasificacion':clasificacion_elegida, 'todos_los_productos':producto})

def ver_productos(request, producto_id):
	producto_elegido = Producto.objects.get(id=producto_id)
	cliente = Cliente.objects.filter(producto = producto_elegido)
	return render(request, 'cliente.html', {'mi_producto':producto_elegido, 'mi_cliente':cliente})

def ver_clientes(request, cliente_dni):
	cliente_elegido = Cliente.objects.get(dni=cliente_dni)
	factura = Factura.objects.filter(cliente = cliente_elegido)
	return render(request, 'factura.html', {'el_cliente':cliente_elegido, 'factura_cliente':factura})


# Create your views here.
