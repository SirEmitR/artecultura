from django import forms
from django.http import request

from .models import Deporte

class FormularioDeporte(forms.ModelForm):

    class  Meta:
        model = Deporte
        fields= ["nombre", "descripcion"]