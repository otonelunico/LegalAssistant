from django.shortcuts import render, redirect
from django.views import View
from .forms import CrearCasoJuridicoForm

# Create your views here.



class CrearCasoJuridico(View):
    template = 'casojuridico/nuevo.html'
    def get(self, request, **kwargs):
        form = CrearCasoJuridicoForm()
        print(form)
        return render(request, self.template, locals())