from django import forms
from .peticion import Peticion

#clases de formularios
class ContactForm(forms.Form):
    #atributos de contacto
    tiposmj = forms.ChoiceField(label="Tipo de peticion", required=True, choices=Peticion, widget=forms.Select(attrs={'class':'form-control'}))
    usuario = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu nombre'}))
    correo = forms.EmailField(label="Correo electronico", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu correo'}))
    mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'rows':'3','class':'form-control','placeholder':'Escribe tu mensaje'}))