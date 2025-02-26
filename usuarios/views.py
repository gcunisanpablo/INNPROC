from django.http import JsonResponse

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from .forms import (
    LoginForm,  # otros formularios que se necesiten
)
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.conf import settings

import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings


# Inicio de sesion
def login(request):
    error = None  # Inicializamos el mensaje de error
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.filter(username=cd["username"]).first()

            if user is not None:
                user_auth = authenticate(
                    request, username=cd["username"], password=cd["password"]
                )
                if user_auth is not None:
                    if user.is_active:
                        auth_login(request, user_auth)
                        return redirect("mapa-procesos")
                    else:
                        error = "Inicio de sesión inválido"
                else:
                    error = "Contraseña incorrecta"
            else:
                error = "No se encuentra la cuenta"
    else:
        form = LoginForm()

    return render(request, "index.html", {"form": form, "error": error})


# Funcion verificacion logeado custom
def login_required_custom(view_func):
    return login_required(view_func, login_url="login")


# Cerrar sesion
@never_cache
@login_required_custom
def custom_logout(request):
    logout(request)
    return redirect(reverse("login"))


@login_required
def cambiar_contraseña(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Evita que se cierre la sesión
            return JsonResponse(
                {"success": True, "message": "Contraseña cambiada correctamente."}
            )
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = PasswordChangeForm(request.user)

    return JsonResponse({"success": False, "message": "Método no permitido."})


def password_recovery(request):
    if request.method == "POST":
        # Obtener los datos del cuerpo de la solicitud
        data = json.loads(request.body)
        email = data.get("email")

        if not email:
            return JsonResponse(
                {"success": False, "error": "Correo electrónico no proporcionado."}
            )

        # Enviar el correo con el mensaje de recuperación
        subject = "Restablecer Contraseña"
        message = f"El usuario con correo {email} necesita restablecer su contraseña ya que la olvidó."
        from_email = settings.DEFAULT_FROM_EMAIL  # o el correo de tu preferencia
        recipient_list = [
            "gestionycalidad@unisanpablo.edu.co"
        ]  # Correo del destinatario

        try:
            send_mail(subject, message, from_email, recipient_list)
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Método no permitido."})
