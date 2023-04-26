from django.shortcuts import render,redirect
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
    foto=cuento.foto.url
    
    return render(request, 'AppCuentos/verCuento.html', {'categoria':categoria,'titulo':titulo,'subtitulo':subtitulo,'cuerpo':cuerpo,'autor':autor,'fecha':fecha,'foto':foto})

'''@login_required
def nuevaFoto(request, id):
    if request.method=="POST":
        form=FotoForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            foto=Foto()
            foto.cuento=Cuento.objects.get(id=id)
            foto.foto=request.FILES["foto"]
            
            foto.save()

            cuentos=Cuento.objects.all()
            return render(request,"AppCuentos/inicioCuentos.html", {"mensaje":'Cuento cargado con éxito','cuentos':cuentos})

        else:
            return render(request, "AppCuentos/verCuento.html", {"mensaje":"Error al agregar foto"})
    else:
        form=FotoForm()
        return render(request, "AppCuentos/agregarFoto.html", {"form": form})
'''
@login_required
def nuevoCuento(request):
    
    if request.method =='POST':
        form=CuentoForm(request.POST,request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            
            cuento=Cuento()
            cuento.fecha=datetime.date.today()
            cuento.categoria=info['categoria']
            cuento.autor=request.user
            cuento.titulo=info["titulo"]
            cuento.subtitulo=info['subtitulo']
            cuento.cuerpo=info['cuerpo']
            cuento.foto=request.FILES["foto"]
            
            cuento.save()

            return redirect('inicioCuentos')
        else:
            return render(request,"AppCuentos/inicioCuentos.html", {"mensaje":'Error al agregar el cuento'})
         
    else:
        form=CuentoForm()
        return render(request, "AppCuentos/nuevoCuento.html", {"form": form})   

def inicioCuentos(request):
    cuentos=Cuento.objects.all()
    
    return render(request,"AppCuentos/inicioCuentos.html", {'cuentos':cuentos})