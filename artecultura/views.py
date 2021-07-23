from django.http import HttpResponse

from django.shortcuts import render, resolve_url

from django.core.mail import EmailMessage

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.views import generic

def inicio (request ):
    return render(request, "inicio.html")

def enviarCorreo( asunto, mensaje, nombre):
    correo = EmailMessage(asunto, mensaje, to=[nombre])
    correo.send()

def ingresar(request):
    f = AuthenticationForm()
    if request.method == "POST":
        f = AuthenticationForm(data = request.POST)
        if f.is_valid():
            u = request.POST["username"]
            p = request.POST["password"]

            '''Autenticacion'''
            user = authenticate(username = u, password = p)
            if user is not None:
                login(request, user)
                request.session["variableSesion"] = u
    return render(request, "Login.html", {"formulario": f})

def registrarUsuario(request):
    f = UserCreationForm()
    if request.method == "POST":
        f = UserCreationForm(data = request.POST)
        if f.is_valid():
            user = f.save()
    f.fields["username"].help_text = None
    f.fields["password1"].help_text = None
    f.fields["password2"].help_text = None
    return render(request,"agregarUsuario.html", {"formulario": f})

def salir(request):
    logout(request)
    return HttpResponse("Fueraaaa")