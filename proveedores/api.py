from .models import Proveedor
from .serializers import ProveedorSerializer
from rest_framework import viewsets, permissions

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer