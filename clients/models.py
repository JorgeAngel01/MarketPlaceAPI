from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Proveedores(models.Model):
    id_proveedor = models.SmallAutoField()
    descripcion = models.CharField(max_length=400)

    def __str__(self):
        return self.descripcion
    
class Restaurantes:
    id_restaurante = models.SmallAutoField()
    descripcion = models.CharField(max_length=400)
    location = models.PointField()

    def __str__(self):
        return self.descripcion
    
class Clientes:
    id_cliente = models.SmallAutoField()

    def __str__(self):
        return self.id_cliente
