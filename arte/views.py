from typing import Generic
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from arte.formulario import FormularioArte
from django.views import generic
from arte.models import Arte
# Create your views here.
def inicio(request):
    return render(request, "Arte.html")

def agregar(request):
    formulario = FormularioArte()
    if request.method == "POST":
        formulario = FormularioArte(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("/")
    return render(request, "Arte.html", {"form":formulario}) 

#======================================================================
class listaActividad(generic.ListView):
    model = Arte
    context_object_name = 'Actividades'
    template_name = 'Arte.html'