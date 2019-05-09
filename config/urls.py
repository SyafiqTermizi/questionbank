from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('questionbank.dashboards.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/', include('questionbank.users.urls')),
    path('invites/', include('questionbank.invites.urls')),
    path('admin/', admin.site.urls),
]
