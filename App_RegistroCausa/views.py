import datetime
from django.shortcuts import render, redirect
from django.views import View
from .forms import CrearCasoJuridicoForm
from App_Base.models import Solicitud, CasoJuridico
# Create your views here.

def StrToDate(texto):
    date = texto.split('/')[2] + '-' + texto.split('/')[0] + '-' + texto.split('/')[1]
    date = datetime.datetime.strptime(str(date), "%Y-%m-%d").date()
    return date

class CrearCasoJuridico(View):
    template = 'casojuridico/nuevo.html'
    def get(self, request, **kwargs):
        solicitud = Solicitud.objects.get(id=kwargs['id'])
        form = CrearCasoJuridicoForm()
        print(form)
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        solicitud = Solicitud.objects.get(id=kwargs['id'])
        form = CrearCasoJuridicoForm(request.POST)
        print(form)
        if form.is_valid():
            casojuridico = CasoJuridico(
                solicitud_id=solicitud.id,
                nombre_caso=form.cleaned_data['nombre_caso'],
                n_rol_tibunal=form.cleaned_data['n_rol_tibunal'],
                estado='En Proceso',
                instancia=form.cleaned_data['instancia'],
                fecha_inicio=StrToDate(form.cleaned_data['fechas'].split(' - ')[0]),
                fecha_termino=StrToDate(form.cleaned_data['fechas'].split(' - ')[1])
                )
            casojuridico.save()
            return redirect('listacasos')
        return render(request, self.template, locals())

class ListadoDeCasos(View):
    template = 'casojuridico/listadodecasos.html'
    def get(self, request):
        casos = CasoJuridico.objects.all()
        solicitudes = Solicitud.objects.all()
        return render(request, self.template, locals())


