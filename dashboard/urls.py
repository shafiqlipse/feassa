from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *



urlpatterns = [
    path("dashboard/", Dashboard, name="dashboard"),
    path("albums/", album_list, name="album_list"),
    path("albums/<int:school_id>/<int:sport_id>/<str:gender>/", album_detail, name="album_detail"),
    path("albums/<int:school_id>/<int:sport_id>/<str:gender>/pdf/", album_pdf, name="album_pdf"),
    path('athletes/summary/export/', athlete_summary_csv, name='athlete_summary_csv'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
