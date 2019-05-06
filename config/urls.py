from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('accounts', include('allauth.urls')),
    path('users/', include('questionbank.users.urls')),
    path('admin/', admin.site.urls),
]
