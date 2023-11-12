from rest_framework import serializers
from .models import Restaurante

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('id', 'propietario', 'nombre', 'descripcion', 'latitud', 'longitud')