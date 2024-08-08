from django.conf import settings

from django.conf.urls.static import static
from django.urls import path
from .views import *

# from competition.views import get_teams


urlpatterns = [
    path("dashboard/", Dashboard, name="dashboard"),
    path("schools/", Schools, name="schools"),
    path("allschools/", AllSchools, name="allschools"),
    path("school/<int:id>", SchoolDetail, name="school"),
    # ------------Athletes-------------------
    path("athletes/", Athletes, name="athletes"),
    path("athlete/<int:id>", athleteDetail, name="athlete"),
    path("athleteupdate/<int:id>", athleteUpdate, name="athleteupdate"),
    path("deleteathlete/<int:id>", deleteAthlete, name="athletedelete"),
    # ------------Officials-------------------
    path("allofficials/", allOfficials, name="allofficials"),
    path("officials/", Officials, name="officials"),
    path("Offs/", TOfficials, name="Offs"),
    path("official/<int:id>", officialDetail, name="official"),
    path("officialupdate/<int:id>", officialUpdate, name="officialupdate"),
    path("deleteofficial/<int:id>", deleteOfficial, name="officialdelete"),
    # --------------------------------
    path("Athletes/", TAthletes, name="Athletes"),
    #  # team
    path("new_team/", create_team, name="new_team"),
    path("updateteam/<int:id>", update_team, name="updategteam"),
    path("teams/", teamlist, name="teams"),
    path("allteams/", allteamlist, name="allteam_s"),
    path("team/<int:id>", team_details, name="steam"),
    path("team_accred/<int:id>", teamAccreditation, name="team_accred"),
    path("team_cert/<int:id>", TeamCert, name="team_cert"),
    path("deleteteam/<int:id>", delete_team, name="delete_team"),
    # path("deleteteam/<int:id>", delete_team, name="delete_team"),
    path("activity-log/", activity_log_view, name="activity_log"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
