from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'autor', 'contenido', 'calificacion', 'fecha', 'restaurante', 'proveedor', 'producto')