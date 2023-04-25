from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def nuevoCuento(request):
    
    if request.method =='POST':
        form=CuentoForm(request.POST)
        form2=FotoForm(request.POST, request.FILES)

        if form.is_valid() and form2.is_valid():
            info=form.cleaned_data
            
            cuento=Cuento()
            cuento.fecha=datetime.date.today()
            cuento.categoria=info['categoria']
            cuento.autor=request.user
            cuento.titulo=info["titulo"]
            cuento.subtitulo=info['subtitulo']
            cuento.cuerpo=info['cuerpo']
            
            cuento.save()

            info2=form2.cleaned_data
            foto=Foto()
            foto.foto=request.FILES["foto"]
            foto.titulo= info2['titulo']

            foto.save()
            
        else:
            return render(request,"AppCuentos/inicioCuentos.html", {"mensaje":'Error al agregar el cuento'})
        
        return render(request,"AppCuentos/inicioCuentos.html", {"mensaje":'Cuento cargado con éxito'})
    else:
        form=CuentoForm()
        form2=FotoForm()
        return render(request, "AppCuentos/nuevoCuento.html", {"form": form,'form2':form2})   
