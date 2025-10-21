from .models import MovimientoUsuario
from django.utils.deprecation import MiddlewareMixin

class RegistroActividadMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            path = request.path
            # Excluir admin, static y media
            if path.startswith(('/admin/', '/static/', '/media/')):
                return None

            MovimientoUsuario.objects.create(
                usuario=request.user,
                accion=f"Accedió a {path}",
                ip=self.obtener_ip(request),
            )
        return None

    def obtener_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
