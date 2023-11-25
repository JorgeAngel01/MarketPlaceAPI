from django.db import models
from restaurantes.models import Restaurante
from proveedores.models import Proveedor
from productos import catalogos

class Producto(models.Model):    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=200, null=True, blank=True)
    categoria = models.CharField(
        max_length=2,
        choices=catalogos.CATEGORIAS,
        default=0,
    )
    estado = models.CharField(
        max_length=2,
        choices=catalogos.ESTADO,
        default=1,
    )
    promedio_calific = models.DecimalField(
        max_digits=3,
        decimal_places=2, 
        null=True, 
        blank=True
    )
    restaurantes = models.ManyToManyField(Restaurante, blank=True)
    proveedores = models.ManyToManyField(Proveedor, blank=True)
    
    def __str__(self):
        return self.nombre
