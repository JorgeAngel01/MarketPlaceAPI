from .models import Orden, OrdenItem
from .serializers import OrdenSerializer, OrdenItemSerializer
from rest_framework import viewsets, permissions

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrdenSerializer

class OrdenItemViewSet(viewsets.ModelViewSet):
    queryset = OrdenItem.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrdenItemSerializer