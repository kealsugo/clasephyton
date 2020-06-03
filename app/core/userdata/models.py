from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos

# Create your models here.
#creeacion de la estructura del modelo de datos



class Roles(models.Model):
    RoleName = models.CharField(max_length = 50, verbose_name = "nombre")

    class Meta:
        verbose_name = "perfil usuario"
        verbose_name_plural = "perfiles"

     #funcion para llamar atributos
    def __str__(self):
        return self.RoleName

class DatosUser(models.Model):
    UserDNI = models.CharField(max_length = 20)
    NombUser = models.CharField(max_length = 200, null=True, verbose_name="nombre usuario")
    ApeUser = models.CharField(max_length = 200, null=True, verbose_name="apellido usuario")
    ProfeUser = models.CharField(max_length = 100, null=True, verbose_name="profesion usuario")
    FotoUser = models.ImageField(default='user.png', verbose_name="foto perfil", upload_to = "img/perfiles")
    TeleUser = models.CharField(max_length = 20, verbose_name="telefono usuario")
    GenUser = models.CharField(max_length = 20, choices = Generos, default = "Otros", verbose_name = "genero")
    AddData = models.DateTimeField(auto_now_add = True, null=True, verbose_name = "fecha de ingreso")
    Modifiat = models.DateTimeField(auto_now = True, null=True, verbose_name = "fecha de cambios")

    class Meta:
        verbose_name = "datos usuarios"
        verbose_name_plural = "informacion"

    def __str__(self):
        return self.NombUser

class HabiUser(models.Model):
    NombHabi = models.CharField(max_length = 100, null=True, verbose_name = "nombre")
    DescHabi = RichTextField(max_length = 2000, null=True, default= "Estudiante", verbose_name="Descripcion de la habilidad")

    class Meta:
        verbose_name = "habilidades de usuario"
        verbose_name_plural = "competencias"

    def __str__(self):
        return self.NombHabi

class DetaRoles(models.Model):
    IDRole = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name = "Identificador de rol")
    IDUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name="identificador de usuaio")
    AddUser = models.DateTimeField(auto_now_add = True, null=True, verbose_name = "fecha")
    UdtUser = models.DateTimeField(auto_now = True, null=True, verbose_name = "fecha de actualizacion de usuario")
    EstaRol = models.CharField(max_length = 10, null=True, verbose_name = "estado")

    class Meta:
        verbose_name = "Roles de usuaio"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.EstaRol

class Rates(models.Model):
    IDHabilidades = models.ForeignKey(HabiUser, on_delete = models.CASCADE, verbose_name = "Identificador de habilidad")
    IDUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Identificador de usuario")
    Porcentaje = models.DecimalField(max_digits = 2, null=True, decimal_places = 1, verbose_name = "porcentaje") #99,9
    UdtHabil = models.DateTimeField(auto_now = True, null=True, verbose_name = "fecha de actualizacion habilidad")

    class Meta:
        verbose_name = "niveles de usuarios"
        verbose_name_plural = "niveles de usuarios"

    def __unicode__(self):
        return self.IDUser
        

 
