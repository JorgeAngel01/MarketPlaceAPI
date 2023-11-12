from rest_framework import serializers
from .models import Orden, OrdenItem

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ('id', 'cliente', 'fecha', 'precio_total', 'estado')

class OrdenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenItem
        fields = ('id', 'orden', 'producto', 'cantidad')