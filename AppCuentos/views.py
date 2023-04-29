from django.shortcuts import render,redirect
from .models import *
from .forms import *
from AppUsuarios.models import *
from AppUsuarios.views import *
from AppUsuarios.forms import *
from django.http import HttpResponse

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
    id=cuento.id
    
    return render(request, 'AppCuentos/verCuento.html', {'id':id, 'categoria':categoria,'titulo':titulo,'subtitulo':subtitulo,'cuerpo':cuerpo,'autor':autor,'fecha':fecha,'foto':foto})

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
    if len(cuentos)==0:
        mensaje="Aún no hay cuentos cargados... Inspirate y da el primer paso"
    else:
        mensaje=''
    return render(request,"AppCuentos/inicioCuentos.html", {'cuentos':cuentos,'mensaje':mensaje})

def buscarCuento(request):
    titulo=request.GET['titulo']
    if titulo!='':
        cuentos=Cuento.objects.filter(titulo__icontains=titulo)
        return render(request, 'AppCuentos/inicioCuentos.html',{'cuentos':cuentos})
    else:
        return render(request, 'AppCuentos/buscarCuento.html',{'mensaje':'Ingrese una palabra clave a buscar'})

def mensajeAlAutor(request, id):
    cuento=Cuento.objects.get(id=id)
    if request.method =='POST':
        form=MensajeAlAutorForm(request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            mensaje=Mensaje()
            mensaje.remitente=request.user
            mensaje.titulo=info["titulo"]
            mensaje.destinatario=cuento.autor
            mensaje.contenido=info["contenido"]
            mensaje.fecha=datetime.date.today()
            
            mensaje.save()

            return render(request,"AppUsuarios/inicioUsuarios.html", {"mensaje":'Mensaje enviado con éxito',"avatar":obtenerAvatar(request)})
    else:
        form=MensajeAlAutorForm()
        return render(request, "AppCuentos/mensajeAlAutor.html", {"form": form,"avatar":obtenerAvatar(request)})


def eliminarCuento(request, id):
    cuento = Cuento.objects.get(id=id)
    cuento.delete()

    return render(request, "AppCuentos/inicioCuentos.html", {'mensaje':f'Cuento "{cuento.titulo}" eliminado '})

def misCuentos(request):
    cuentos=Cuento.objects.all()
    if len(cuentos)==0:
        mensaje="Aún no hay cuentos cargados... Inspirate y da el primer paso"
    else:
        mensaje=''
    return render(request,"AppCuentos/misCuentos.html", {'cuentos':cuentos,'mensaje':mensaje})