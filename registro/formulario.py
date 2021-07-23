from django import forms
from django.http import request

from .models import persona

class FormularioPersona(forms.ModelForm):

    class  Meta:
        model = persona
        fields= ["nombre", "apellidos", "sexo"]