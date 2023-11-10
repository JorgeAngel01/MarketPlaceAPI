from rest_framework import serializers
from .models import Restaurante

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('id', 'nombre', 'descripcion', 'latitud', 'longitud')