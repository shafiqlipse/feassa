# myapp/middleware.py

from django.utils.timezone import now
from .models import UserActivityLog

class ActivityLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the response first
        response = self.get_response(request)

        # Check if the user is authenticated and the request path is not for static or media files
        if request.user.is_authenticated and not request.path.startswith(('/static/', '/media/')):
            UserActivityLog.objects.create(
                user=request.user,
                activity=f"Visited {request.path}",
                timestamp=now()
            )

        return response
