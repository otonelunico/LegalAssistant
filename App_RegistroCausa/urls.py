from django.urls import path
from .views import CrearCasoJuridico

urlpatterns = [
    path('nuevo/<int:id>/', CrearCasoJuridico.as_view(), name='nuevocasojuridico'),
]