# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Clasificacion(models.Model):
	tipo = models.CharField(max_length=20)

def __str__(self):
	return ' {}.'.format(self.tipo)

class Producto(models.Model):
	nombre = models.CharField(max_length=20)
	clasificacion = models.ForeignKey(Clasificacion)
	precio = models.IntegerField(null=False)

def __str__(self):
	return 'el producto, {} es un/a {}.'.format(self.nombre, self.clasificacion.tipo)

class Cliente(models.Model):
	dni = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	producto = models.ForeignKey(Producto)

def __str__(self):
	return '{} {}, DNI: {}.'.format(self.apellido, self.nombre, self.dni)

class Factura(models.Model):
	cliente = models.ForeignKey(Cliente)
	producto = models.ForeignKey(Producto)

def __str__(self):
	return 'El cliente, {} {} compro {} por el precio de {}.'.format(self.cliente.apellido, self.cliente.nombre, self.producto.nombre, self.producto.precio)




# Create your models here.
