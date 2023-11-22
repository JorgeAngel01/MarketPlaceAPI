from django.db import models
from django.contrib.auth.models import User
from proveedores import catalogos

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(
        max_length=400, 
        null=True, 
        blank=True
    )
    categoria = models.CharField(
        max_length=2,
        choices=catalogos.CATEGORIAS,
        default=0,
    )
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
