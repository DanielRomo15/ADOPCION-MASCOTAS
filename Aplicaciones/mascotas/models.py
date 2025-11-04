from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# personas

class Personas(models.Model):
    id_personas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.IntegerField(unique=True)
    correo_electronico = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id_cliente}: {self.nombre} {self.apellido}"

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fechaIngreso = models.DateField()
    categoria = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.TextField(null=True, blank=True)
    logo = models.FileField(upload_to='productos', null=True, blank=True)
    activo = models.BooleanField(default=True)  # Nuevo campo

    def __str__(self):
        return f"{self.id_producto}: {self.nombre} ({self.categoria}) [{self.fechaIngreso}] Stock: {self.stock}"


# Empresa

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    ruc = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=30)
    email = models.EmailField()
    logo = models.FileField(upload_to='empresa', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.ruc})"
#VENTAS
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Venta #{self.id_venta} - {self.cliente} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey('Producto', on_delete=models.PROTECT)
    nombre_producto = models.CharField(max_length=200)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo al crear
            self.nombre_producto = self.producto.nombre
            self.precio_unitario = self.producto.precio_unitario
            self.subtotal = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_producto} x {self.cantidad} (Venta #{self.venta.id_venta})"
