from django.shortcuts import render
from .models import *
from .forms import *
from AppUsuarios.models import *
from AppUsuarios.views import *

# Create your views here.

def verCuento(request, id):
    
    cuento=Cuento.objects.get(id=id)
    categoria=cuento.categoria
    titulo=cuento.titulo
    subtitulo=cuento.subtitulo
    cuerpo=cuento.cuerpo
    autor=cuento.autor
    fecha=cuento.fecha
    imagen=Foto.objects.get(cuento_id=id)
    foto=imagen.foto.url
    
    return render(request, {'categoria':categoria,'titulo':titulo,'subtitulo':subtitulo,'cuerpo':cuerpo,'autor':autor,'fecha':fecha,'foto':foto})

@login_required
def nuevaFoto(request):
    if request.method=="POST":
        form=FotoForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            foto=Foto()
            foto.cuento=info['cuento']
            foto.foto=request.FILES["foto"]
            
            foto.save()

            cuentos=Cuento.objects.all()
            return render(request,"AppCuentos/inicioCuentos.html", {"mensaje":'Cuento cargado con éxito','cuentos':cuentos})

        else:
            return render(request, "AppCuentos/verCuento.html", {"mensaje":"Error al agregar foto"})
    else:
        form=FotoForm()
        return render(request, "AppCuentos/agregarFoto.html", {"form": form})

@login_required
def nuevoCuento(request):
    
    if request.method =='POST':
        form=CuentoForm(request.POST)

        if form.is_valid():
            info=form.cleaned_data
            
            cuento=Cuento()
            cuento.fecha=datetime.date.today()
            cuento.categoria=info['categoria']
            cuento.autor=request.user
            cuento.titulo=info["titulo"]
            cuento.subtitulo=info['subtitulo']
            cuento.cuerpo=info['cuerpo']
            
            cuento.save()

        
            return render(request,"AppCuentos/inicioCuentos.html", {"mensaje":'Cuento agregado'})
        else:
            return render(request,"AppCuentos/inicioCuentos.html", {"mensaje":'Error al agregar el cuento'})
         
    else:
        form=CuentoForm()
        return render(request, "AppCuentos/nuevoCuento.html", {"form": form})   

def inicioCuentos(request):
    cuentos=Cuento.objects.all()
    
    return render(request,"AppCuentos/inicioCuentos.html", {'cuentos':cuentos})