from django.urls import path
from . import views
from .views import UserProfileView

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('user/', UserProfileView.as_view(), name='user-profile'),  # Make sure this matches the path
]
