from django.db import models
from restaurantes.models import Restaurante
from proveedores.models import Proveedor

class Producto(models.Model):
    ESTADO = [ ('1', 'En Stock'), ('2', 'Agotado'), ]
    
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Agregar Imagen
    # Agregar Categoria
    estado = models.CharField(
        max_length=2,
        choices=ESTADO,
        default=1,
    )
    restaurantes = models.ManyToManyField(Restaurante, blank=True)
    proveedores = models.ManyToManyField(Proveedor, blank=True)
    # restaurante = models.ForeignKey(
    #     Restaurante, 
    #     on_delete=models.CASCADE, 
    #     null=True, 
    #     blank=True
    # )
    # proveedor = models.ForeignKey(
    #     Proveedor, 
    #     on_delete=models.CASCADE, 
    #     null=True, 
    #     blank=True
    # )
    
    def __str__(self):
        return self.nombre
