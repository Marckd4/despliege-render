from django.db import models

# Create your models here.
from django.db import models

class MovimientoUsuario(models.Model):
    # tus campos aquí
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    accion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)  # <- agregar esto si quieres guardar IP
