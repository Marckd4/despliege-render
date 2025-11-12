# usuarios/utils.py
from .models import MovimientoUsuario

def registrar_movimiento(usuario, accion, descripcion='', ip=None):
    if usuario.is_authenticated:
        MovimientoUsuario.objects.create(
            usuario=usuario,
            accion=accion,
            descripcion=descripcion,
            ip=ip
        )
