from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import CrearCasoJuridico,ListadoDeCasos

urlpatterns = [
    path('lista/', login_required(ListadoDeCasos.as_view()), name='listacasos'),
    path('nuevo/<int:id>/', login_required(CrearCasoJuridico.as_view()), name='nuevocasojuridico'),
]