from django.db import models
from django.contrib.auth.models import User
from restaurantes.models import Restaurante
from proveedores.models import Proveedor
from productos.models import Producto

class Review(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=300, null=True, blank=True)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Review por {self.autor} calificando {self.rating} estrellas"
