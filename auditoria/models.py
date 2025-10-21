# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# class MovimientoUsuario(models.Model):
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     accion = models.CharField(max_length=255)  # descripción de la acción
#     fecha = models.DateTimeField(auto_now_add=True)
#     ip = models.GenericIPAddressField(null=True, blank=True)
#     detalles = models.TextField(blank=True)

#     def __str__(self):
#         return f"{self.usuario} - {self.accion} - {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
