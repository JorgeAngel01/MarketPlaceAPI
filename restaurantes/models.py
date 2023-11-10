from django.db import models

class Restaurante(models.Model):
    # id_restaurante = models.SmallAutoField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    # ubicacion = models.PointField()
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.nombre
