from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import *
from dashboard.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", user_login, name="login"),
    path("auth/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("get_athletes/", get_athletes, name="get_athletes"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
