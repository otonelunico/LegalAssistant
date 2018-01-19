from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class TipoUser(models.Model):
    titulo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(null=False, blank=True)

    def __str__(self):
        return '{}'.format(self.titulo)


class EstadoUser(models.Model):
    titulo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(null=False, blank=True)

    def __str__(self):
        return '{}'.format(self.titulo)


class ExtraUser(models.Model):
    user = models.OneToOneField(User, null=False, blank=True, on_delete=models.CASCADE, primary_key=True)
    rut = models.CharField(max_length=10, unique=True)
    tipo = models.ForeignKey(TipoUser, null=False, blank=True, default=1, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoUser, null=False, blank=True, default=1, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.user.first_name + ' ' + self.user.last_name)


class GastoOficina(models.Model):
    nombre_gasto = models.CharField(max_length=25)
    descripcion = models.TextField(null=False, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre_gasto)


class Gastos_User(models.Model):
    user = models.ForeignKey(ExtraUser, blank=True, on_delete=models.CASCADE)
    gasto = models.ForeignKey(GastoOficina, blank=True, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    valor = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField(null=False, blank=True)

    def __str__(self):
        return '{}'.format(self.gasto)


class Reunion(models.Model):
    fecha_inicio = models.CharField(max_length=40, default=False)
    fecha_final = models.CharField(max_length=40, default=False)
    todo_Dia = models.BooleanField(default=False)
    color = models.CharField(max_length=6, default='ffffff')
    tema_reunion = models.CharField(max_length=30)
    observacion = models.TextField(null=False, blank=True)
    caso_juridico = models.IntegerField(default=0)
    url = models.CharField(max_length=200, default=False)

    def __str__(self):
        return '{}'.format(self.tema_reunion + ' ' + str(self.fecha_inicio)+ ' ' + str(self.fecha_final))


class UserReunion(models.Model):
    user = models.ForeignKey(ExtraUser, blank=True, on_delete=models.CASCADE)
    reunion = models.ForeignKey(Reunion, blank=True, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.reunion)


class Cliente(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.rut + ' ' + self.nombre)


class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return '{}'.format(self.nombre)


class TemaJuridico(models.Model):
    materia = models.ForeignKey(Materia, blank=True, on_delete=models.CASCADE)
    nombre_tema = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombre_tema + ' ' + self.materia.nombre)


class Solicitud(models.Model):
    tema_juridico = models.ForeignKey(TemaJuridico, blank=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, blank=True, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=50)
    observaciones = models.TextField()
    demandado_nombre = models.CharField(max_length=100, null=True)
    demandado_rut = models.CharField(max_length=100, null=True)
    demandado_telefono = models.CharField(max_length=100, null=True)
    demandado_direccion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{}'.format(self.cliente.nombre + ' ' + self.tema_juridico.nombre_tema)


def generate_path(instance, filename):
    return os.path.join("documents", str(instance.rut), filename)


class DocumentoSolicitud(models.Model):
    solicitud = models.ForeignKey(Solicitud, blank=True, on_delete=models.CASCADE)
    #nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    rut = models.CharField(max_length=10)
    docfile = models.FileField(upload_to=generate_path, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.solicitud.cliente.nombre + ' ' + self.rut)


class Documentacion(models.Model):

    tema_juridico = models.ForeignKey(TemaJuridico, blank=True, on_delete=models.CASCADE)
    #nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    docfile = models.FileField(upload_to=generate_path, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.rut)


class CasoJuridico(models.Model):
    solicitud = models.ForeignKey(Solicitud, blank=True, on_delete=models.CASCADE)
    nombre_caso = models.CharField(max_length=40)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    n_rol_tibunal= models.CharField(max_length=80)
    estado = models.CharField(max_length=50)
    instancia = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.solicitud.cliente.nombre + ' ' + self.nombre_caso)


class UserCaso(models.Model):
    user = models.ForeignKey(ExtraUser, blank=True, on_delete=models.CASCADE)
    caso_juridico = models.ForeignKey(CasoJuridico, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user.user.username + ' ' + self.caso_juridico.nombre_caso)


class Tribunal(models.Model):
    caso_juridico = models.ForeignKey(CasoJuridico, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.nombre)


class Etapa(models.Model):
    caso = models.ForeignKey(CasoJuridico, blank=True, on_delete=models.CASCADE)
    nombre_etapa = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    descripcion = models.TextField()
    fecha_termini = models.TimeField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre_etapa + ' ' + self.caso.nombre_caso)


class Actividad(models.Model):
    etapa = models.ForeignKey(Etapa, blank=True, on_delete=models.CASCADE)
    nombre_actividad = models.CharField(max_length=50)
    fecha_hora = models.DateTimeField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre_actividad)


class Notificacion(models.Model):
    user = models.ForeignKey(ExtraUser, blank=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    enlace = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.titulo)


