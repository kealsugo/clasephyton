from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from userdata.models import DatosUser


# Create your models here.
class TipoDocu(models.Model):
    NombTipoDoc = models.CharField(max_length = 50, null=True, verbose_name = "tipo documento")

    class Meta:
        verbose_name = "Tipo documento"
        verbose_name_plural = "Tipo documento"

     #funcion para llamar atributos
    def __str__(self):
        return self.NombTipoDoc

class CategProye(models.Model):
    Lenguaje = models.CharField(max_length = 150, null=True, verbose_name = "lenguaje")
    MotorDB = models.CharField(max_length = 150, null=True, verbose_name = "motor BD")
    Arquitectura = models.CharField(max_length = 150, null=True, verbose_name = "Arquitectura")

    class Meta:
        verbose_name = "datos proyecto"
        verbose_name_plural = "Arquitectura"

     #funcion para llamar atributos
    def __str__(self):
        return self.Lenguaje

class Proyectos(models.Model):
    IDCategProye = models.ForeignKey(CategProye, on_delete = models.CASCADE, verbose_name = "Identificador de categoria")
    NombProye = models.CharField(max_length = 200, null=True, verbose_name="nombre proyecto")
    DescProye = models.CharField(max_length = 200, null=True, verbose_name="descripcion proyecto")
    ImgProye = models.ImageField(default='proye.png', verbose_name="imagen proyecto", upload_to = "imgproyecto/img")
    FechaIni = models.DateTimeField(auto_now_add = True, null=True, verbose_name="fecha de inicio")
    FechaFin = models.DateTimeField(auto_now = True, null=True, verbose_name="fecha de finalizacion")
    UrlRepo = models.CharField(max_length = 200, null=True, verbose_name="repositorio")
    EstaProye = models.CharField(max_length = 200, null=True, verbose_name="estado")

    class Meta:
        verbose_name = "datos del proyecto"
        verbose_name_plural = "informacion"

    def __str__(self):
        return self.NombProye

class Documentos(models.Model):
    IDTipoDocu = models.ForeignKey(TipoDocu, on_delete = models.CASCADE, verbose_name = "Identificador de tipo de documento")
    IDProyectos = models.ForeignKey(Proyectos, on_delete = models.CASCADE, verbose_name = "Identificador de proyecto")
    IDusuaio = models.ForeignKey(DatosUser, on_delete = models.CASCADE, verbose_name = "Identificador de usuario")
    NombDoc = models.CharField(max_length = 100, null=True, verbose_name = "nombre documento")
    PathDoc = models.CharField(max_length = 100, null=True, verbose_name = "pathdocu")

    class Meta:
        verbose_name = "Documentos"
        verbose_name_plural = "Documentos"

     #funcion para llamar atributos
    def __str__(self):
        return self.NombDoc
