from django.contrib.auth import authenticate, login, logout as auth_logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm


class Login(View):
    template = 'base/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template, locals())

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = 'Nombre de usuario o contraseña son incorrecto'
        return render(request, self.template, locals())

class Logout(View):

    def get(self, request):
        auth_logout(request)
        return redirect('login')


class Home(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template, locals())


class CalendarioView(View):
    template = 'calendario.html'

    def get(self, request):
        return render(request, self.template, locals())

