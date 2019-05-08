from django.urls import path

from .views import UserListView, UserUpdateView, UserProfileView, UserDeleteView


app_name = 'users'
urlpatterns = [
    path('', UserListView.as_view(), name='list'),
    path('<int:pk>/', UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
    path('profile/', UserProfileView.as_view(), name='profile')
]
