from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *



urlpatterns = [
    # path("dashboard/", Dashboard, name="dashboard"),
    path("schools/", Schools, name="schools"),
    path("allschools/", AllSchools, name="allschools"),
    path("school/<int:id>", SchoolDetail, name="school"),
    path("deleteschool/<int:id>", deleteSchool, name="deleteschool"),
    # ------------Athletes-------------------
    path("athletes/", Athletes, name="athletes"),
    path("athlete/<int:id>", athleteDetail, name="athlete"),
    path("qathlete/<int:id>", qr_code, name="qathlete"),
    path("athleteupdate/<int:id>", athleteUpdate, name="athleteupdate"),
    path("deleteathlete/<int:id>", deleteAthlete, name="athletedelete"),
    # ------------Officials-------------------
    path("allofficials/", allOfficials, name="allofficials"),
    path("officials/", Officials, name="officials"),
    path("official/<int:id>", officialDetail, name="official"),
    path("officialupdate/<int:id>", officialUpdate, name="officialupdate"),
    path("deleteofficial/<int:id>", deleteOfficial, name="officialdelete"),
    # ------------Reports Athletes-------------------
    path("athletesreport/", athletesReports, name="athletesreport"),
    path("officialsreport/", officialsReports, name="officialsreport"),
    path("positionsreport/", positionsReports, name="positionsreport"),
    path("export_acsv/", export_acsv, name="export_acsv"),
    path("export_scsv/", export_scsv, name="export_scsv"),
    path("export_ocsv/", export_ocsv, name="export_ocsv"),
    # path("export_ocsv/", export_ocsv, name="export_ocsv"),
    # path("export_ocsv/", export_ocsv, name="export_ocsv"),
    path("register_position/", manage_positions, name="register_position"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
