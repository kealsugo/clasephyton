from django.contrib import admin

# Register your models here.
from .models import TipoDocu, CategProye, Proyectos, Documentos

class TipoDocuMode(admin.ModelAdmin):
    list_display = ["NombTipoDoc"]

    class Meta:
        model = TipoDocu

admin.site.register(TipoDocu)

class CategProyeMode(admin.ModelAdmin):
    list_display = ["Lenguaje"]

    class Meta:
        model = CategProye

admin.site.register(CategProye)

class ProyectosMode(admin.ModelAdmin):
    list_display = ["NombProye"]

    class Meta:
        model = Proyectos

admin.site.register(Proyectos)

class DocumentosMode(admin.ModelAdmin):
    list_display = ["NombDoc"]

    class Meta:
        model = Documentos

admin.site.register(Documentos)