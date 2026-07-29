from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts.views import loginUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginUser, name='login'),
    path('dashboard/', include('dashboard.urls')),
    path('auth/', include('accounts.urls')),
    path('schools/', include('school.urls')),
    path('committee/', include('comittee.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
