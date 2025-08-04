from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

# from competition.views import get_teams


urlpatterns = [
 
    path("success/", success, name="success"),
    path("noc/", committee, name="noc"),
    path("committees/", committees, name="committees"),
    path("committees_reports/", comitteesReports, name="committees_reports"),
    path("committee/<int:id>", committeeDetail, name="committee"),
    # path("delenoc/<int:id>", deleteNoc, name="delenoch"),
    path("media/", media, name="media"),
    path("media_list/", mediaList, name="media_list"),
    path("media_accreditation/", mediaAccreditation, name="media_accreditation"),
    path("media/<int:id>", mediaDetail, name="media_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
