from django.urls import path
from usuarios import views
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("login")),  # Redirigir a login
    path("login/", views.login, name="login"),  # Iniciar sesion
    path("logout/", views.custom_logout, name="logout"),  # Cerrar sesion
    path("cambiar-contraseña/", views.cambiar_contraseña, name="cambiar_contraseña"),
    path("password_recovery/", views.password_recovery, name="password_recovery"),
]
