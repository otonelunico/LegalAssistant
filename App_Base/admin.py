from django.contrib import admin
from .models import TipoUser, ExtraUser, EstadoUser, GastoOficina, Gastos_User, Actividad ,\
    Etapa, CasoJuridico, TemaJuridico, Materia, Documentacion, Tribunal, UserCaso, Cliente, \
    Reunion, Solicitud, UserReunion, DocumentoSolicitud

#
admin.site.register(ExtraUser)
admin.site.register(TipoUser)
admin.site.register(EstadoUser)
admin.site.register(GastoOficina)
admin.site.register(Gastos_User)
admin.site.register(Actividad)
admin.site.register(Etapa)
admin.site.register(CasoJuridico)
admin.site.register(Tribunal)
admin.site.register(TemaJuridico)
admin.site.register(DocumentoSolicitud)
admin.site.register(UserReunion)
admin.site.register(Solicitud)
admin.site.register(Reunion)
admin.site.register(Materia)
admin.site.register(Documentacion)
admin.site.register(UserCaso)
admin.site.register(Cliente)
