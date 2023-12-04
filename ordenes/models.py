from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

class Orden(models.Model):
    ESTADO = [ 
        ('0', 'Editando'),
        ('1', 'Pedido Realizado'),
        ('2', 'Enviado'),
        ('3', 'En Reparto'),
        ('4', 'Entregado'),
    ]
    
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado = models.CharField(
        max_length=2,
        choices=ESTADO,
        default=0,
    )
    
    def __str__(self):
        return f"Orden de {self.cliente} realizada el {self.fecha.date()} a las {self.fecha.hour}:{self.fecha.minute}"

class OrdenItem(models.Model):
    ESTADO = [ 
        ('0', 'Procesando'),
        ('1', 'Cancelado'),
        ('2', 'Aceptado'),
    ]
    
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    estado = models.CharField(
        max_length=2,
        choices=ESTADO,
        default=0,
    )
    
    def __str__(self):
        return f"Producto {self.producto} en {self.orden}"

