from django import forms

class CrearCasoJuridicoForm(forms.Form):
    nombre_caso = forms.CharField(max_length=40)
    fechas = forms.CharField(max_length=30, required=False)
    n_rol_tibunal= forms.CharField(max_length=80)
    estado = forms.CharField(max_length=50, required=False)
    instancia = forms.CharField(max_length=100)