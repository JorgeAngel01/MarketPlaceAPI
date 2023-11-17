from .models import Proveedor
from django.contrib.auth.models import User
from .serializers import ProveedorSerializer
from rest_framework import viewsets, permissions, views, response, status

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer

class GetProveedorView(views.APIView):

    def get(self, request, username):
        try:
            propietario = User.objects.get(username=username)
            
            proveedores = Proveedor.objects.filter(propietario=propietario)
            
            serializer = ProveedorSerializer(proveedores, many=True)
            return response.Response(serializer.data)

        except User.DoesNotExist:
            return response.Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)