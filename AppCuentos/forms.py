from django import forms
import datetime
from .models import *

categorias=(('Fantasia','Fantasia'),('Micro-Relato','Micro-Relato'),('Ciencia Ficción','Ciencia Ficción'),('Policial','Policial'),('Fábula','Fábula'),('Terror','Terror'))

class CuentoForm(forms.Form):
    categoria=forms.ChoiceField(choices=categorias,label='Seleccione una categoria')
    titulo=forms.CharField(label='Título')
    subtitulo=forms.CharField(label='Subtítulo')
    cuerpo=forms.CharField(label='Mil palabras')
    foto=forms.ImageField(label='Foto')

class buscarPorCategoriaForm(forms.Form):
    categoria=forms.ChoiceField(choices=categorias,label='Seleccione una categoria')