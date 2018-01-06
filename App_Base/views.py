from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

class Home(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template, locals())


class Login(View):
    template = 'base/login.html'

    def get(self, request):
    		#form = AuthenticationForm()
        return render(request, self.template, locals())

    def post(self, request, **kwargs):
	    form = AuthenticationForm(request.POST)
	    if form.is_valid():
	    	print('True')
	    else:
	        form = RegistroForm()
	        print(form.is_valid())
	        print(form.errors)
	    return render(request, self.template, locals())