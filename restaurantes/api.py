from .models import Restaurante
from .serializers import RestauranteSerializer
from rest_framework import viewsets, permissions

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RestauranteSerializer