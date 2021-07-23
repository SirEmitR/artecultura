from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from deportes.formulario import FormularioDeporte
from django.views import generic
from .models import Deporte
# Create your views here.
def inicio(request):
    return render(request, "Deportes.html")

def agregar(request):
    formulario = FormularioDeporte()
    if request.method == "POST":
        formulario = FormularioDeporte(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("/")
    return render(request, "Deportes.html", {"form":formulario}) 
#======================================================================
class listaActividad(generic.ListView):
    model = Deporte
    context_object_name = 'Actividades'
    template_name = 'Deportes.html'