from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
from userdata.models import DatosUser
from django.views.generic import ListView

# Create your views here.
class HomePageView(TemplateView):

    template_name = "index.html"


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'tituloini':'hola','titulo2':'como estas','DM':'Digital Market',
        'DescripcionDM':'Digital market es un plataforma de ventas para un supermercado acogiendo un diseño acogedor y fácil de usar para el usuario, la plataforma contará con diversas opciones tanto para el usuario y administrador.'
        })


class NosotrosPageView(ListView):
    model = DatosUser
    template_name = "nosotros.html"


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulous':'que tal','titulo2':'como estas'})  

class datos(ListView):
    model = DatosUser
    template_name = "nosotros.html"

def contacto(request):
    formContact = ContactForm()
    #validacion formulario
    if request.method == "POST":
        formContact = ContactForm(data=request.POST)
        if formContact.is_valid():
            tiposmj = request.POST.get('tiposmj','')
            usuario = request.POST.get('usuario','')
            correo = request.POST.get('correo','')
            mensaje = request.POST.get('mensaje','')

            #enviar mensaje
             # Creamos el objeto con las variables del formulario:
            email = EmailMessage(
                "RepoDevelopers: tienes un nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\nTipo de Mensaje:{}\n{}".format(usuario, correo, tiposmj, mensaje),
                "no-contestar@inbox.mailtrap.io",
                ["kealsugo@gmail.com"],
                reply_to=[correo]
            )
            # Enviamos el correo:
            try:
                email.send()
                # Se envia el correo:
                return redirect(reverse('contacto')+"?ok")
            except:
                # No se ha enviado el correo:
                return redirect(reverse('contacto')+"?fail")


    return render(request, 'contacto.html', {'formulario':formContact})              