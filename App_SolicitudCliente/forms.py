from django import forms


class NuevoClienteForm(forms.Form):

    rut = forms.CharField(max_length=12)
    nombre = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.CharField(max_length=50)


class DocumentacionForm(forms.Form):
    tema_juridico = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=10)
    docfile = forms.FileField()
    
class NuevaSolicitud(forms.Form):
    tema_juridico = forms.CharField(max_length=50)
    cliente = forms.CharField(max_length=50)
    observaciones = forms.Textarea()
    demandado_nombre = forms.CharField(max_length=100)
    demandado_rut = forms.CharField(max_length=100)
    demandado_telefono = forms.CharField(max_length=100)
    demandado_direccion = forms.CharField(max_length=100)