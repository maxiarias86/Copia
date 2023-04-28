from django.shortcuts import render
from AppUsuarios.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppUsuarios.forms import *
from django.contrib.auth.decorators import login_required
import datetime

def inicioUsuarios(request):
    return render (request, 'AppUsuarios/inicioUsuarios.html',{"avatar":obtenerAvatar(request)})

def about(request):
    return render(request, 'AppUsuarios/about.html',{"avatar":obtenerAvatar(request)})
# LOGIN

def login_request(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario=info['username']
            contra=info['password']

            user=authenticate(username=usuario,password=contra)

            if user is not None:
                login(request, user)
                return render(request,'AppUsuarios/inicioUsuarios.html', {'mensaje':f"Bienvenido {usuario}","avatar":obtenerAvatar(request)})
            else:
                return render(request,'AppUsuarios/login.html', {"avatar":obtenerAvatar(request),'form':form, 'mensaje':"Usuario y/o Contraseña incorrectos"})
        else:
            return render(request,'AppUsuarios/login.html', {"avatar":obtenerAvatar(request),'form':form, 'mensaje':"Usuario y/o Contraseña incorrecto."})
    
    form= AuthenticationForm()

    return render (request, 'AppUsuarios/login.html', {'form':form,"avatar":obtenerAvatar(request)})

def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, 'AppUsuarios/inicioUsuarios.html', {"mensaje":f"Usuario {username} creado correctamente","avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppUsuarios/register.html", {"form": form, "mensaje":"Error al crear el usuario","avatar":obtenerAvatar(request)})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppUsuarios/register.html", {"form": form,"avatar":obtenerAvatar(request)})

#PERFILES
@login_required
def editarUser(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            password=info["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request, "AppUsuarios/inicioUsuarios.html", {"mensaje":f"Usuario {usuario.username} editado correctamente","avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppUsuarios/editarUser.html", {"form": form, "nombreusuario":usuario.username,"avatar":obtenerAvatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppUsuarios/editarUser.html", {"form": form, "nombreusuario":usuario.username,"avatar":obtenerAvatar(request)})

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=PerfilForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            perfil=Perfil()
            perfil.user=request.user
            perfil.descripcion=info['descripcion']
            perfil.pagina=info['pagina']

            perfilViejo=Perfil.objects.filter(user=request.user)
            if len(perfilViejo)>0:
                perfilViejo[0].delete()

            perfil.save()
            return render(request, "AppUsuarios/inicioUsuarios.html", {"mensaje":"Perfil editado correctamente","avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppUsuarios/inicioUsuarios.html", {"mensaje":"Error en el fomulario","avatar":obtenerAvatar(request)})
    else:
        form=PerfilForm()
        return render(request, "AppUsuarios/editarPerfil.html", {"form": form, "nombre_usuario":usuario.username,"avatar":obtenerAvatar(request)})
 

@login_required
def obtenerAvatar(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatars/default.png"


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            
            avatarViejo=Avatar.objects.filter(user=request.user) #Esto sirve para borrar uno viejo si lo hubiera tenido
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppUsuarios/inicioUsuarios.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppUsuarios/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppUsuarios/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})

@login_required
def verMiPerfil(request):
    username=request.user.username
    email=request.user.email
    avatar=obtenerAvatar(request)
    perfil=Perfil.objects.filter(user=request.user.id)
    if len(perfil)!=0:
        descripcion=perfil[0].descripcion
        pagina=perfil[0].pagina
    else:
        descripcion=''
        pagina=''
    
    return render(request, 'AppUsuarios/verMiPerfil.html', {'username':username,'email':email,'avatar':avatar,'descripcion':descripcion,'pagina':pagina})


def verPerfil(request, id):
    user=User.objects.get(id=id)
    username=user.username
    email=user.email
    perfil=Perfil.objects.filter(user=user.id)
    if len(perfil)!=0:
        descripcion=perfil[0].descripcion
        pagina=perfil[0].pagina
    else:
        descripcion=''
        pagina=''
    avatares=Avatar.objects.filter(user=user.id)
    if len(avatares)!=0:
        avatar=avatares[0].imagen.url
    else:
        avatar="/media/avatars/default.png"

    return render(request, 'AppUsuarios/verPerfil.html', {'username':username,'email':email,'avatar':avatar,'descripcion':descripcion,'pagina':pagina})

    

# MENSAJERIA

@login_required
def responder(request, id):
  mensaje_recibido=Mensaje.objects.get(id=id)
  
  if request.method =='POST':
    form=RespuestaForm(request.POST)
    if form.is_valid():
      info=form.cleaned_data      
      respuesta=Mensaje()
      respuesta.remitente=request.user
      respuesta.destinatario=mensaje_recibido.remitente
      respuesta.titulo='Re-'+mensaje_recibido.titulo
      respuesta.contenido=info["contenido"]
      respuesta.fecha=datetime.date.today()
            
      respuesta.save()

      return render(request,"AppUsuarios/inicioUsuarios.html", {"mensaje":'Mensaje respondido con éxito'})
  else:
    form=RespuestaForm()
    return render(request, "AppUsuarios/responderMensaje.html", {"form": form})

@login_required
def nuevoMensaje(request):
    
    if request.method =='POST':
        form=MensajeForm(request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            mensaje=Mensaje()
            mensaje.remitente=request.user
            mensaje.titulo=info["titulo"]
            mensaje.destinatario=info["destinatario"]
            mensaje.contenido=info["contenido"]
            mensaje.fecha=datetime.date.today()
            
            mensaje.save()

            return render(request,"AppUsuarios/inicioUsuarios.html", {"mensaje":'Mensaje enviado con éxito',"avatar":obtenerAvatar(request)})
    else:
        form=MensajeForm()
        return render(request, "AppUsuarios/nuevoMensaje.html", {"form": form,"avatar":obtenerAvatar(request)})
    
@login_required
def mensajes(request):
    mensajes=Mensaje.objects.all()

    return render (request, 'AppUsuarios/mensajesRecibidos.html', {'mensajes':mensajes})

@login_required
def mensajesEnviados(request):
    mensajes=Mensaje.objects.all()

    return render (request, 'AppUsuarios/mensajesEnviados.html', {'mensajes':mensajes})

@login_required
def buscarUsuario(request):
    username=request.GET['username']
    
    if username!='':
        usuarios=User.objects.filter(username__icontains=username)
        return render(request, 'AppUsuarios/resultadosBusqueda.html',{'usuarios':usuarios})
    else:
        return render(request, 'AppUsuarios/buscarUsuarios.html',{'mensaje':'Ingrese un nombre a buscar'})

