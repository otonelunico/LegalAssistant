from django import forms

class CrearCasoJuridicoForm(forms.Form):
    nombre_caso = forms.CharField(max_length=40)
    fecha_inicio = forms.CharField(max_length=10)
    fecha_termino = forms.CharField(max_length=10)
    n_rol_tibunal= forms.CharField(max_length=80)
    estado = forms.CharField(max_length=50)
    instancia = forms.CharField(max_length=100)