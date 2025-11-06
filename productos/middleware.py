# productos/middleware.py

from django.utils import timezone
from django.contrib.auth.models import User

class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            User.objects.filter(id=request.user.id).update(last_login=timezone.now())
        return self.get_response(request)
