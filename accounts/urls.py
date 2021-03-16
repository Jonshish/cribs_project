from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("password_recovery", views.password_recovery, name="password_recovery"),
    path("password_reset", views.password_reset, name="password_reset"),
    path("password_reset_sent", views.password_reset_sent, name="password_reset_sent"),
]
