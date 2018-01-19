from django.urls import path
from .views import RegistroUsuario, ListadoUsuario, EditarUsuario, Cambio

urlpatterns = [
    path('nuevo/', RegistroUsuario.as_view(), name='registrousuario'),
    path('lista/', ListadoUsuario.as_view(), name='listausuario'),
    path('editar/<int:user>/', EditarUsuario.as_view(), name='editarusuario'),
    path('cambio/<str:cambio>/<int:id>/<int:select>/', Cambio.as_view(), name='cambiouser'),
]
