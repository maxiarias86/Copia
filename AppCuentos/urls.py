from django.urls import path
from AppUsuarios.views import *
from AppCuentos.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", inicioCuentos, name="inicioCuentos"),
    path("verCuento/<id>", verCuento, name="verCuento"),
    path('nuevoCuento', nuevoCuento, name='nuevoCuento'),
    path('buscarCuento', buscarCuento, name='buscarCuento'),
    path('mensajeAlAutor/<id>', mensajeAlAutor, name='mensajeAlAutor'),
    path('eliminarCuento/<id>', eliminarCuento, name='eliminarCuento'),
    path('misCuentos/', misCuentos, name='misCuentos'),
    
    
]