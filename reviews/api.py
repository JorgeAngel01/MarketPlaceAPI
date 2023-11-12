from .models import Producto
from .serializers import ReviewSerializer
from rest_framework import viewsets, permissions

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReviewSerializer