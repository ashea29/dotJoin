from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'accounts'

urlpatterns = [
    # Login / Log Out
    path('login/', auth_views.LoginView.as_view(
         template_name = 'accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
         template_name = 'thanks.html'), name='logout'),
    # Sign Up
    path("signup/", views.SignUp.as_view(
         template_name = 'accounts/signup.html'), name="signup")
]