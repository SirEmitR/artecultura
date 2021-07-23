from django.db import models

# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(max_length=2, choices=[('H', "Hombre"), ('M', "Mujer")], default="H")
    correo = models.CharField(max_length=100, default="example@gmail.com")