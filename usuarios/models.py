# usuarios/models.py
from django.db import models
from django.contrib.auth.models import User

class MovimientoUsuario(models.Model):
    ACCIONES = [
        ('CREAR', 'Creación'),
        ('MODIFICAR', 'Modificación'),
        ('ELIMINAR', 'Eliminación'),
        ('IMPORTAR', 'Importación masiva'),
        ('ELIMINAR_TODOS', 'Eliminación total'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    accion = models.CharField(max_length=50, choices=ACCIONES)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.accion} ({self.fecha:%d/%m/%Y %H:%M})"
