from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

# from competition.views import get_teams


urlpatterns = [
 
    path("success/", success, name="success"),
    # path("addmember/", committee, name="addmember"),
    path("committees/", committees, name="committees"),
    path("all_committee_members/", all_committee_members, name="all_committee_members"),
    path("committees_reports/", comitteesReports, name="committees_reports"),
    path("all_comitteesReports/", all_comitteesReports, name="all_comitteesReports"),
    path("committee/<int:id>", committeeDetail, name="committee"),
    path("committee/<int:id>/edit", edit_committee, name="edit_committee"),
    path("committee/<int:id>/delete", delete_committee, name="delete_committee"),
    path("media/<int:id>/delete", delete_media, name="delete_media"),
    
    
    # path("delenoc/<int:id>", deleteNoc, name="delenoch"),
    # path("delenoc/<int:id>", deleteNoc, name="delenoch"),
    # path("delenoc/<int:id>", deleteNoc, name="delenoch"),
    # path("media/", media, name="media"),
    path("media_list/", media_list, name="media_list"),
    path("mediall_media_lista_list/", all_media_list, name="all_media_list"),
    path("media_accreditation/", mediaAccreditation, name="media_accreditation"),
    path("all_mediaAccreditation/", all_mediaAccreditation, name="all_media_accreditation"),
    path("media/<int:id>", mediaDetail, name="media_detail"),
    path("success/<int:id>", media_success, name="media_success"),
    path("match_official_success/<int:id>", match_official_success, name="match_official_success"),
    path("committee_success/<int:id>", committee_success, name="committee_success"),
    
    
    # path("delenoc/<int:id>", deleteNoc, name="delenoch"),
    # path("delenoc/<int:id>", deleteNoc, name="delenoch"),
    # path("delenoc/<int:id>", deleteNoc, name="delenoch"),
    # path("add_match_official/", add_match_official, name="add_match_official"),
    path("match_officials_list/", match_official_list, name="match_officials_list"),
    path("all_match_official/", all_match_official, name="all_match_official"),
    path("match_officials_accreditation/", OfficiatingOfficialsAccreditation, name="match_officials_accreditation"),
    path("all_match_officials_accreditation/", all_OfficiatingOfficialsAccreditation, name="all_match_officials_accreditation"),
    path("match_official/<int:id>", match_official_detail, name="match_official"),
    path("match_official_success/<int:id>", match_official_success, name="match_official_success"),
    path("delete_match_official/<int:id>", delete_match_official, name="delete_match_official"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
