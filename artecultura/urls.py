"""artecultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.conf.urls import url

from artecultura.views import inicio, enviarCorreo, ingresar, registrarUsuario as agregar, salir
from arte.views import agregar as agregarArte, inicio as inicioArte, listaActividad
from deportes.views import agregar as agregarDeporte, inicio as inicioDeporte, listaActividad as lD
from registro.views import listaUsuarios, registro as r
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^registro$", listaUsuarios.as_view()),
    url(r"^registro/agregar", r),
    url(r"^$", inicio), #Que inicie con ningun caracter y termine con ningun caracter'''
    url(r"^arte/agregar$", agregarArte),
    url(r"^deportes/agregar$", agregarDeporte),
    url(r"^arte$", listaActividad.as_view()),
    url(r"^deportes$", lD.as_view()),
    url(r"^correo$", enviarCorreo),
    url(r'^login$', ingresar),
    url(r"^usuario/agregar$", agregar),
    url(r"^logout", salir)
]
