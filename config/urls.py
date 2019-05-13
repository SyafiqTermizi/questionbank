from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('questionbank.dashboards.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/', include('questionbank.users.urls')),
    path('invites/', include('questionbank.invites.urls')),
    path('subjects/', include('questionbank.subjects.urls')),
    path('questions/', include('questionbank.questions.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
