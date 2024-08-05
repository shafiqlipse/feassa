from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

# from competition.views import get_teams


urlpatterns = [
 
    path("logout/", user_logout, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
