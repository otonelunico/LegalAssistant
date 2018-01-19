from django.urls import path
from .views import CrearCliente, CrearSolicitud, CrearSolisitudAgregarDocumentos, ListarSolicitudes, ListaCliente

urlpatterns = [
    path('', CrearCliente.as_view(), name='cliente'),
    path('solicitudes/', ListarSolicitudes.as_view(), name='listadolicitudes'),
    path('solicitud/nueva/', CrearSolicitud.as_view(), name='nuevasolicitud'),
    path('solicitud/<int:id>/', CrearSolisitudAgregarDocumentos.as_view(), name='nuevasolicituddocumentos'),
   # path('', ListaCliente.as_view(), name='listadoclientes'),
]