from django import forms
from django.http import request

from .models import Arte

class FormularioArte(forms.ModelForm):

    class  Meta:
        model = Arte
        fields= ["nombre", "descripcion"]