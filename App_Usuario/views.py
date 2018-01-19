from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from App_Base.models import ExtraUser, TipoUser, EstadoUser
from django.contrib.auth.models import User
from .forms import RegistroForm
from django.db.models import Q


class RegistroUsuario(View):
    template = 'users/nuevo.html'

    def get(self, request):
        form = RegistroForm()
        tipo = TipoUser.objects.all()
        estado = EstadoUser.objects.all()
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        tipo = TipoUser.objects.all()
        estado = EstadoUser.objects.all()
        form = RegistroForm(request.POST)
        error = {}
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['usuario']).count() > 0:
                error['usuario'] = 'Usuario ya existe'
            elif User.objects.filter(username=form.cleaned_data['usuario']).count() < 1:
                contrasena = form.cleaned_data['contrasena1']
                if contrasena == form.cleaned_data['contrasena2'] and 7 < len(contrasena) < 20:
                    user = User.objects.create(username=form.cleaned_data['usuario'],
                                               first_name=form.cleaned_data['nombre'],
                                               last_name=form.cleaned_data['apellidos'],
                                               email=form.cleaned_data['email'])
                    user.set_password(contrasena)
                    user.save()
                    ExtraUser.objects.create(user=user,
                                             rut=form.cleaned_data['rut'],
                                             estado_id=form.cleaned_data['estado'],
                                             tipo_id=form.cleaned_data['tipo'])
                    return redirect('listausuario')
            else:
                print('error form')
                return render(request, self.template, locals())
        else:
            form = RegistroForm()
            print(form.is_valid())
            print(form.errors)
        return render(request, self.template, locals())


class ListadoUsuario(View):
    template = 'users/lista.html'

    def get(self, request):
        usuarios = ExtraUser.objects.all()
        estado = EstadoUser.objects.all()
        tipo = TipoUser.objects.all()
        return render(request, self.template, locals())


class EditarUsuario(View):
    template = 'users/nuevo.html'

    def get(self, request, **kwargs):
        form = RegistroForm()
        user_ = ExtraUser.objects.get(user=kwargs['user'])
        tipo = TipoUser.objects.filter(~Q(id=user_.tipo_id))
        estado = EstadoUser.objects.filter(~Q(id=user_.estado_id))
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
        user_ = ExtraUser.objects.get(user=kwargs['user'])
        user__ = User.objects.get(username=user_.user.username)
        tipo = TipoUser.objects.filter(~Q(id=user_.tipo_id))
        estado = EstadoUser.objects.filter(~Q(id=user_.estado_id))
        form = RegistroForm(request.POST)
        error = {}
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['usuario']).count() > 0 and user__.username != form.cleaned_data['usuario']:
                error['usuario'] = 'Usuario ya existe'
                return render(request, self.template, locals())
            if User.objects.filter(username=user_.user.username).count() > 0:
                contrasena = form.cleaned_data['contrasena1']
                user__.username = form.cleaned_data['usuario']
                user__.first_name = form.cleaned_data['nombre']
                user__.last_name = form.cleaned_data['apellidos']
                user__.email = form.cleaned_data['email']
                if contrasena == form.cleaned_data['contrasena2'] and 7 < len(contrasena) < 20:
                    user__.set_password(contrasena)
                user__.save()
                user_.rut = form.cleaned_data['rut']
                user_.estado_id = form.cleaned_data['estado']
                user_.tipo_id = form.cleaned_data['tipo']
                user_.save()
                return redirect('listausuario')
            else:
                print('error form')
                return render(request, self.template, locals())
        else:
            form = RegistroForm()
            print(form)
            print(form.is_valid())
            print(form.errors)
        return render(request, self.template, locals())

class Cambio(View):
    def get(self, request, **kwargs):
        user = ExtraUser.objects.get(user_id=kwargs['id'])
        if kwargs['cambio']=='estado':
            user.estado_id = kwargs['select']
        if kwargs['cambio']=='tipo':
            user.tipo_id = kwargs['select']
        user.save()
        return redirect('listausuario')