from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets, permissions

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer