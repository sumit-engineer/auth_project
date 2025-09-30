from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView

urlpatterns = [
    path('', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),

    # Use Django's built-in LogoutView
      path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset_password'),


]
