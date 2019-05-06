from django.urls import path

from .views import UserListView, UserUpdateView


app_name = 'users'
urlpatterns = [
    path('', UserListView.as_view(), name='list'),
    path('<int:pk>/', UserUpdateView.as_view(), name='update')
]
