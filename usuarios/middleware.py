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


#registro de usuarios

import datetime
from django.utils import timezone

class LastActivityMiddleware:
    """Guarda la última actividad de cada usuario autenticado"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            now = timezone.now()
            last_activity = request.session.get('last_activity')

            if not last_activity or (now - datetime.datetime.fromisoformat(last_activity)).seconds > 60:
                request.user.last_login = now  # o puedes crear otro campo
                request.user.save(update_fields=['last_login'])
                request.session['last_activity'] = now.isoformat()

        return self.get_response(request)
