from django import forms


class NuevoClienteForm(forms.Form):

    rut = forms.CharField(max_length=12)
    nombre = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.CharField(max_length=50)