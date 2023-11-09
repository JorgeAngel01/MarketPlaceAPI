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

class Categorias_Productos:
    id_categoria= models.SmallAutoField()
    nombre_categoria= models.CharField(max_length=50)

class Productos:
    id_producto = models.SmallAutoField()
    nombre_producto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=400)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True) #Falta configurar para que soporte almacenar las imagenes Os o algo asi
    rating = models.SmallIntegerField()
    categoria = models.ForeignKey(Categorias_Productos, on_delete=models.DO_NOTHING)
    estatus = models.BooleanField()

    def __str__(self):
        return self.nombre_producto

class Estados_Ordenes:
    id_estados_ordenes = models.SmallAutoField()
    nombre_estados_ordenes= models.CharField(max_length=20)

class Ordenes:
    id_orden= models.SmallAutoField()
    id_cliente= models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    #items
    precio_total= models.IntegerField()
    estado=  models.ForeignKey(Estados_Ordenes, on_delete=models.CASCADE)

class Item:
    #id_orden= models.ForeignKey(Ordenes, on_delete=models.DO_NOTHING)
    id_producto= models.ForeignKey(Productos, on_delete=models.DO_NOTHING)
    cantidad= models.IntegerField()

class Resenas:
    id_resena= models.SmallAutoField()
    id_producto= models.ForeignKey(Productos, on_delete=models.DO_NOTHING)
    id_cliente= models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    rating= models.IntegerField()
    texto= models.CharField(max_length=100)