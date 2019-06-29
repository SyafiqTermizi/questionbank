from django.urls import path
from django.views.decorators.cache import cache_page

from .views import Dashboard


app_name = 'dashboards'
urlpatterns = [
    path('', cache_page(60*30)(Dashboard.as_view()), name='dashboard')
]
