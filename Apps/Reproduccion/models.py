import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

def images_path():
    return os.path.join(settings.STATICFILES_DIRS, 'img/album_photos')

# Create your models here.
class Cancion(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.DecimalField(max_digits=4, decimal_places=2)
    autor = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

class Album(models.Model):
    nombre = models.CharField(max_length=30)
    duracion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    foto = models.ImageField(upload_to=images_path, max_length=100, null=True, blank=True)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    disquera = models.ForeignKey('Disquera', on_delete=models.CASCADE)

class Disquera(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=100, null=True)

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=200, unique=True, null=True, blank=True)

class Playlist(models.Model):
    isPublic = models.BooleanField(default=False)
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class PlaylistCanciones(models.Model):
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    cancion = models.ForeignKey('Cancion', on_delete=models.CASCADE)