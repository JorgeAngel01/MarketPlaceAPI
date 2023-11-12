from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

class Orden(models.Model):
    ESTADO = [ 
        ('1', 'Entregada'),
        ('2', 'Cancelada'),
        ('3', 'Procesando'),
    ]
    
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(
        max_length=2,
        choices=ESTADO,
        default=1,
    )
    
    def __str__(self):
        return f"Orden de {self.cliente} realizada el {self.fecha}"

class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"Producto {self.producto} en {self.orden}"

