from django.db import models
from django.contrib.auth.models import User
class Tipo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)  #Unique = true; indica que el dato es unico en la tabla 

    def __str__(self):
        return self.nombre

class Segmento(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# Create your models here.
