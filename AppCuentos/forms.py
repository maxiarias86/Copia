from django import forms
import datetime

categorias=['Fantasia','Micro-Relato','Ciencia Ficción','Policial','Fábula','Terror']

class CuentoForm(forms.Form):
    categoria=forms.ChoiceField(choices=categorias,label='Seleccione una categoria')
    titulo=forms.CharField(label='Título')
    subtitulo=forms.CharField(label='Subtítulo')
    cuerpo=forms.CharField('Mil palabras')

class FotoForm(forms.Form):
    foto=forms.ImageField(label='Foto')
