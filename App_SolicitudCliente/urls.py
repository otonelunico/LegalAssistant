from django.urls import path
from .views import CrearCliente, CrearSolicitud

urlpatterns = [
    path('nuevo/', CrearCliente.as_view(), name='nuevocliente'),
    path('solicitud/', CrearSolicitud.as_view(), name='nuevasolicitud'),
]