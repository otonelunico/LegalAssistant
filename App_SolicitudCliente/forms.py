from django import forms


class NuevoClienteForm(forms.Form):

    rut = forms.CharField(max_length=12)
    nombre = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.CharField(max_length=50)


class DocumentacionForm(forms.Form):
    #rut = forms.CharField(max_length=10, required=False)
    docfile1 = forms.FileField(required=False)
    docfile2 = forms.FileField(required=False)
    docfile3 = forms.FileField(required=False)
    docfile4 = forms.FileField(required=False)
    docfile5 = forms.FileField(required=False)
    docfile6 = forms.FileField(required=False)
    docfile7 = forms.FileField(required=False)
    docfile8 = forms.FileField(required=False)
    docfile9 = forms.FileField(required=False)
    docfile0 = forms.FileField(required=False)
    
class NuevaSolicitudForm(forms.Form):
    tema_juridico = forms.CharField(max_length=50)
    cliente = forms.CharField(max_length=50)
    observaciones = forms.Textarea()
    demandado_nombre = forms.CharField(max_length=100)
    demandado_rut = forms.CharField(max_length=100)
    demandado_telefono = forms.CharField(max_length=100)
    demandado_direccion = forms.CharField(max_length=100)
