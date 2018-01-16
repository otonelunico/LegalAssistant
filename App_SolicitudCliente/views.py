from django.shortcuts import render
from django.views import View
from .forms import NuevoClienteForm, NuevaSolicitud
from App_Base.models import Cliente, DocumentoSolicitud, TemaJuridico, Solicitud

# Create your views here.

class CrearCliente(View):
    template = 'client/nuevo.html'

    def get(self, request):
        clientes = Cliente.objects.all()
        form = NuevoClienteForm()
        return render(request, self.template, locals())

    def post(self, request):
        form = NuevoClienteForm(request.POST)
        clientes = Cliente.objects.all()
        if form.is_valid():
            if clientes.filter(rut=form.cleaned_data['rut']).count()<1:
                Cliente.objects.create(
                    rut=form.cleaned_data['rut'],
                    nombre=form.cleaned_data['nombre'],
                    tipo=form.cleaned_data['tipo'],
                    email=form.cleaned_data['email'],
                    telefono=form.cleaned_data['telefono'],
                    direccion=form.cleaned_data['direccion']
                )
                form=NuevoClienteForm()
            error = 'Usuario ya existe'
        print(form)
        return render(request, self.template, locals())

class CrearSolicitud(View):
    template = 'client/solicitud.html'
    def get(self, request):
        clientes = Cliente.objects.all()
        tema_juridico = TemaJuridico.objects.all()
        form = NuevaSolicitud()
        print(form)
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        clientes = Cliente.objects.all()
        form = NuevaSolicitud(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            doc = Solicitud(
            )
            doc.save(form)
        else:
            tema_juridico = TemaJuridico.objects.all()
            print(form)
            print(form.is_valid())
            print(form.errors)
        return render(request, self.template, locals())