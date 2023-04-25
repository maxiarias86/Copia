from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ponerlas en el fomulario como choice categorias=['Fantasia','Micro-Relato','Ciencia Ficción','Policial','Fábula','Terror']

class Cuento(models.Model):
    fecha=models.DateField()
    imagen=models.ImageField()
    categoria=models.CharField(max_length=20)
    titulo=models.CharField(max_length=50, unique=True)
    subtitulo=models.CharField(max_length=100)
    cuerpo=models.CharField(max_length=100000)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)

