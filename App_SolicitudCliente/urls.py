from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import CrearCliente, CrearSolicitud, CrearSolisitudAgregarDocumentos, ListarSolicitudes, ListaCliente

urlpatterns = [
    path('', login_required(CrearCliente.as_view()), name='cliente'),
    path('solicitudes/', login_required(ListarSolicitudes.as_view()), name='listadolicitudes'),
    path('solicitud/nueva/', login_required(CrearSolicitud.as_view()), name='nuevasolicitud'),
    path('solicitud/<int:id>/', login_required(CrearSolisitudAgregarDocumentos.as_view()), name='nuevasolicituddocumentos'),
   # path('', ListaCliente.as_view(), name='listadoclientes'),
]