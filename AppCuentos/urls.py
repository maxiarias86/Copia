from django.urls import path
from AppUsuarios.views import *
from AppCuentos.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", inicioCuentos, name="inicioCuentos"),
    
    
]