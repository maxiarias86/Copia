from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
import datetime
from AppUsuarios.models import *

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput,help_text='Ingrese una contraseña de 8 o más caracteres')
    password2=forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput,help_text='Repita la contraseña')
   
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email=forms.EmailField(label="Modificar Email")
    password1=forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir nueva contraseña", widget=forms.PasswordInput)
        
    class Meta:
        model=User
        fields=["email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label='Imagen')

class MensajeForm(forms.Form):
    destinatario=forms.ModelChoiceField(queryset=User.objects.all())
    titulo=forms.CharField(label='Asunto')
    contenido=forms.CharField(label='Mensaje de menos de 1000 caracteres')

class MensajeAlAutorForm(forms.Form):
    titulo=forms.CharField(label='Asunto')
    contenido=forms.CharField(label='Mensaje de menos de 1000 caracteres')    

class RespuestaForm(forms.Form):
    contenido=forms.CharField(label='Mensaje de menos de 1000 caracteres')

class PerfilForm(forms.Form):
    descripcion=forms.CharField(label='Ingrese una breve descripción de usted')
    pagina=forms.URLField(label='Ingrese su Webpage')