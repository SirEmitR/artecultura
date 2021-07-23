
from django.shortcuts import redirect, render
from registro.formulario import FormularioPersona
from django.views import generic
from .models import persona


from artecultura.views import enviarCorreo
# Create your views here.
def registro(request):
    formulario =FormularioPersona()
    if request.method == "POST":
        formulario = FormularioPersona(request.POST)
        if formulario.is_valid():
            formulario.save()
            nombre = request.POST["nombre"]
            enviarCorreo("Arte y cultura", "Muchas gracias "+request.POST["apellidos"]+" por registrarte al programa de arte y cultura.", nombre)
            return redirect("/")
    return render(request, "registro.html", {"form":formulario})
    #======================================================================
class listaUsuarios(generic.ListView):
    model = persona
    context_object_name = 'usuarios'
    template_name = 'registro.html'