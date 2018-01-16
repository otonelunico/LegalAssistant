from django.shortcuts import render, redirect
from django.views import View
from .forms import NuevoClienteForm, NuevaSolicitudForm, DocumentacionForm
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
        form = NuevaSolicitudForm()
        print(form)
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        clientes = Cliente.objects.all()
        tema_juridico = TemaJuridico.objects.all()
        form = NuevaSolicitudForm(request.POST)
        if form.is_valid():
            solicitud = Solicitud.objects.create(
                tema_juridico_id=form.cleaned_data['tema_juridico'],
                cliente_id=form.cleaned_data['cliente'],
                estado='Pendiente',
                observaciones=request.POST['observaciones'] ,
                demandado_direccion=form.cleaned_data['demandado_direccion'],
                demandado_nombre=form.cleaned_data['demandado_nombre'],
                demandado_rut=form.cleaned_data['demandado_rut'],
                demandado_telefono=form.cleaned_data['demandado_telefono']
            )
            return redirect('nuevasolicituddocumentos', solicitud.id )
        else:
            print(form)
            print(form.is_valid())
            print(form.errors)
        return render(request, self.template, locals())

class CrearSolisitudAgregarDocumentos(View):
    template = 'client/solicitud_doc.html'
    def get(self, request, **kwargs):
        form = DocumentacionForm()
        print(form)
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        form = DocumentacionForm(request.POST, request.FILES)
        rut = Solicitud.objects.get(id=kwargs['id']).cliente.rut
        if form.is_valid():
            for files in request.FILES:
                if request.FILES[str(files)]:
                    DocumentoSolicitud.objects.create(
                        solicitud_id=kwargs['id'],
                        docfile=request.FILES[str(files)],
                        rut=rut
                    )

        return render(request, self.template, locals())
