from django.urls import path
from .views import RegistroUsuario, ListadoUsuario, EditarUsuario, Cambio
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('nuevo/', login_required(RegistroUsuario.as_view()), name='registrousuario'),
    path('lista/', login_required(ListadoUsuario.as_view()), name='listausuario'),
    path('editar/<int:user>/', login_required(EditarUsuario.as_view()), name='editarusuario'),
    path('cambio/<str:cambio>/<int:id>/<int:select>/', login_required(Cambio.as_view()), name='cambiouser'),
]
