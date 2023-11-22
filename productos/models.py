from django.db import models
from restaurantes.models import Restaurante
from proveedores.models import Proveedor
from productos import catalogos

class Producto(models.Model):
    

    
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Agregar Imagen
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
    restaurantes = models.ManyToManyField(Restaurante, blank=True)
    proveedores = models.ManyToManyField(Proveedor, blank=True)
    
    def __str__(self):
        return self.nombre
