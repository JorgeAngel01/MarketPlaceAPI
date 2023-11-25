from django.db import models
from django.contrib.auth.models import User
from proveedores import catalogos

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    banner = models.URLField(max_length=200, null=True, blank=True)
    icono = models.URLField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
    )
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
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
