from django import forms
from .models import Glosario


class GlosarioForm(forms.ModelForm):
    class Meta:
        model = Glosario
        fields = ["termino", "definicion"]
