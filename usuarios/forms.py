from django import forms


# formulario sesiones
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Usuario", "class": "login__input"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Contraseña", "class": "login__input"}
        )
    )
