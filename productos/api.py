from .models import Producto
from proveedores.models import Proveedor
from restaurantes.models import Restaurante
from .serializers import ProductoSerializer
from rest_framework import viewsets, permissions, views, response, status

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class GetProductosRestauranteView(views.APIView):

    def get(self, request, restaurante_id):
        try:
            restaurante = Restaurante.objects.get(id=restaurante_id)
            
            productos = Producto.objects.filter(restaurantes=restaurante)

            serializer = ProductoSerializer(productos, many=True)
            return response.Response(serializer.data)

        except Restaurante.DoesNotExist:
            return response.Response({'error': 'Restaurante no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class GetProductosProveedorView(views.APIView):

    def get(self, request, proveedor_id):
        try:
            proveedor = Proveedor.objects.get(id=proveedor_id)
            
            productos = Producto.objects.filter(proveedores=proveedor)

            serializer = ProductoSerializer(productos, many=True)
            return response.Response(serializer.data)

        except Proveedor.DoesNotExist:
            return response.Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)