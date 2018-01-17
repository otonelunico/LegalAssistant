from django.urls import path
from .views import CrearCasoJuridico,ListadoDeCasos

urlpatterns = [
    path('lista/', ListadoDeCasos.as_view(), name='listacasos'),
    path('nuevo/<int:id>/', CrearCasoJuridico.as_view(), name='nuevocasojuridico'),
]