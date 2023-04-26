from django import forms
import datetime
from .models import *

categorias=(('1','Fantasia'),('2','Micro-Relato'),('3','Ciencia Ficción'),('4','Policial'),('5','Fábula'),('6','Terror'))

class CuentoForm(forms.Form):
    categoria=forms.ChoiceField(choices=categorias,label='Seleccione una categoria')
    titulo=forms.CharField(label='Título')
    subtitulo=forms.CharField(label='Subtítulo')
    cuerpo=forms.CharField(label='Mil palabras')
    foto=forms.ImageField(label='Foto')