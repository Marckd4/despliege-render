from .models import MovimientoUsuario
from django.utils.deprecation import MiddlewareMixin

class RegistroActividadMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            # Excluir el panel de administración para evitar registros masivos
            if not request.path.startswith('/admin/'):
                MovimientoUsuario.objects.create(
                    usuario=request.user,
                    accion=f"Accedió a {request.path}",
                    ip=self.obtener_ip(request),
                )
        return None

    def obtener_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
