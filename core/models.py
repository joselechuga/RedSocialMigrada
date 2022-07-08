from django.db import models
from datetime import datetime
# Create your models here.


class usuarios(models.Model):
    usuario = models.CharField(max_length=50,verbose_name="nick usuario")
    nombre = models.CharField(max_length=50,verbose_name="nombre usuario")
    password = models.CharField(max_length=50,verbose_name="contraseña")
    password2 = models.CharField(max_length=50,verbose_name="confirmacion contraseña")
    correo = models.EmailField(max_length=50,verbose_name="correo")


    def __str__(self):
        return self.usuario


class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)