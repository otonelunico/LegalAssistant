from django import forms

class ReunionForm(forms.Form):
    fechas = forms.CharField(max_length=80, required=True)
    todo_Dia = forms.BooleanField(required=False)
    color = forms.CharField(max_length=6, required=False)
    tema_reunion = forms.CharField(max_length=30, required=True)
    caso_juridico = forms.IntegerField(required=False)
    observacion = forms.CharField(max_length=500, required=False)