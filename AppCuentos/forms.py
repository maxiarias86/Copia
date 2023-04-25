from django import forms
import datetime
from .models import *

categorias=['Fantasia','Micro-Relato','Ciencia Ficción','Policial','Fábula','Terror']

class CuentoForm(forms.Form):
    categoria=forms.ChoiceField(choices=categorias,label='Seleccione una categoria')
    titulo=forms.CharField(label='Título')
    subtitulo=forms.CharField(label='Subtítulo')
    cuerpo=forms.CharField(label='Mil palabras')

class FotoForm(forms.Form):
    foto=forms.ImageField(label='Foto')
    cuento=forms.ModelChoiceField(queryset=Cuento.objects.all())
