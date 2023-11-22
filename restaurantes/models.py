from django.db import models
from django.contrib.auth.models import User
from restaurantes import catalogos

class Restaurante(models.Model):
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400, null=True, blank=True)
    categoria = models.CharField(
        max_length=2,
        choices=catalogos.CATEGORIAS,
        default=0,
    )
    promedio_calific = models.DecimalField(
        max_digits=3,
        decimal_places=2, 
        null=True, 
        blank=True
    )
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.nombre
