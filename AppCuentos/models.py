from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ponerlas en el fomulario como choice 

class Cuento(models.Model):
    fecha=models.DateField()
    categoria=models.CharField(max_length=20)
    titulo=models.CharField(max_length=50, unique=True)
    subtitulo=models.CharField(max_length=100)
    cuerpo=models.CharField(max_length=100000)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)

class Foto(models.Model):
    foto=models.ImageField(upload_to="fotos") #Hay que ponerlo en la carpeta media como el de avatars
    titulo=models.ForeignKey(Cuento, on_delete=models.CASCADE)