from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.db.models import Q

from App_Base.models import Reunion, CasoJuridico
from .forms import ReunionForm
import datetime

def ParceFecha(tiempo):
    fecha = tiempo.split(' ')
    perse_fecha={}
    perse_fecha['ano'] = fecha[0].split('/')[2]
    perse_fecha['mes'] = int(fecha[0].split('/')[0]) - datetime.datetime.now().month
    perse_fecha['dia'] = fecha[0].split('/')[1]
    if fecha[2] == 'PM':
        perse_fecha['hora'] = int(fecha[1].split(':')[0]) + 12
        if perse_fecha['hora'] == 24:
             perse_fecha['hora'] = 12
    else:
        perse_fecha['hora'] = int(fecha[1].split(':')[0])
        if perse_fecha['hora'] == 12:
            perse_fecha['hora'] = 0
    perse_fecha['minuto'] = fecha[1].split(':')[1]
    return perse_fecha

class CalendarioView(View):
    template = 'calendario/calendario.html'

    def get(self, request):
        calendario = Reunion.objects.filter(user_id=request.user.id, estado=True)
        casos = CasoJuridico.objects.filter(~Q(estado='Terminado'))
        form = ReunionForm()
        for ll in calendario:
            ll.fecha_inicio = ParceFecha(ll.fecha_inicio)
            ll.fecha_final = ParceFecha(ll.fecha_final)

        return render(request, self.template, locals())

    def post(self, request):
        form = ReunionForm(request.POST)
        if form.is_valid():
            if str(form.cleaned_data['color'])=="":
                color = '3a87ad'
            else:
                color = form.cleaned_data['color']
            reunion = Reunion.objects.create(
                    user_id=request.user.id,
                    fecha_inicio=form.cleaned_data['fechas'].split(' - ')[0],
                    fecha_final=form.cleaned_data['fechas'].split(' - ')[1],
                    color=color,
                    tema_reunion=form.cleaned_data['tema_reunion'],
                    observacion=form.cleaned_data['observacion'],
                    url="",
                    caso_juridico=form.cleaned_data['caso_juridico']
                    )
            reunion.url = reunion.id
            reunion.save()
        return redirect('calendario')

class DetalleReunionView(View):
    template = 'calendario/detallereunion.html'

    def get(self, request, **kwargs):
        reunion = Reunion.objects.get(id=kwargs['id'])
        casos = CasoJuridico.objects.filter(~Q(estado='Terminado'))
        if reunion.caso_juridico > 0:
            caso = CasoJuridico.objects.get(id=reunion.caso_juridico)

        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        reunion = Reunion.objects.get(id=kwargs['id'])
        form = ReunionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['color'])
            if str(form.cleaned_data['color'])=="":
                color = '3a87ad'
            else:
                color = form.cleaned_data['color']
            reunion = Reunion(
                    id=reunion.id,
                    user_id=request.user.id,
                    fecha_inicio=form.cleaned_data['fechas'].split(' - ')[0],
                    fecha_final=form.cleaned_data['fechas'].split(' - ')[1],
                    color=color,
                    tema_reunion=form.cleaned_data['tema_reunion'],
                    observacion=form.cleaned_data['observacion'],
                    url=reunion.id,
                    caso_juridico=form.cleaned_data['caso_juridico']
                    )
            reunion.save()
        return redirect('calendario')
