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

class Mascotas(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)
    Raza = models.CharField(max_length=100)
    observaciones = models.TextField(null=True, blank=True)
    logo = models.FileField(upload_to='mascotas', null=True, blank=True)

    def __str__(self):
        return f"{self.id_mascota}: {self.nombre}"



class Adopcion(models.Model):
    id_adpcion = models.AutoField(primary_key=True)
    id_mascotas = models.ForeignKey(Mascota, on_delete=models.PROTECT)
    id_personas = models.ForeignKey(Personas, on_delete=models.PROTECT)
    fecha_adopcion = models.CharField(max_length=150)
    estado_adopcion = models.CharField(max_length=20, unique=True)
    observaciones = models.CharField(max_length=200)
    
    

    def __str__(self):
        return f"{self.nombre} ({self.ruc})"
