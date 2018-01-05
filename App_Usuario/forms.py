from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from App_Base.models import ExtraUser


class RegistroForm(forms.Form):
    usuario = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)
    apellidos = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)
    rut = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    estado = forms.CharField(max_length=20)
    contrasena1 = forms.CharField(max_length=20, required=False)
    contrasena2 = forms.CharField(max_length=20, required=False)


