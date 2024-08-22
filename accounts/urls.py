from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

# from competition.views import get_teams


urlpatterns = [
 
    path("logout/", user_logout, name="logout"),
    path("noc/", offShore, name="noc"),
    path("noc/<int:id>", offShare, name="noch"),
    path("delenoc/<int:id>", deleteNoc, name="delenoch"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
