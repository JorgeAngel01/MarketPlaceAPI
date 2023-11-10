from django.db import models

class Proveedor(models.Model):
    # id_restaurante = models.SmallAutoField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)

    def __str__(self):
        return self.nombre
