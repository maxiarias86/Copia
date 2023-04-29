from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    user=models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=20000,blank=True,null=True)
    pagina=models.URLField(max_length=200,blank=True,null=True)

    def __str__(self):
        return f'Usuario: {self.user} - Descripcion: {self.descripcion} - WebPage: {self.pagina}'

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Mensaje(models.Model):
    remitente=models.ForeignKey(User, related_name="remitente", on_delete=models.CASCADE)
    destinatario=models.ForeignKey(User, related_name="destinatario", on_delete=models.CASCADE)
    titulo=models.CharField(max_length=30)
    contenido=models.CharField(max_length=1000)
    fecha=models.DateField()

    def __str__(self):
        return f'El día {self.fecha}, {self.remitente} escribió a {self.destinatario} bajo el título {self.titulo}: {self.contenido}'