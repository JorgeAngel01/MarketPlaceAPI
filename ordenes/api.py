from .models import Orden, OrdenItem
from django.contrib.auth.models import User
from .serializers import OrdenSerializer, OrdenItemSerializer
from rest_framework import viewsets, permissions, views, response, status

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrdenSerializer

class OrdenItemViewSet(viewsets.ModelViewSet):
    queryset = OrdenItem.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrdenItemSerializer

class GetOrdenView(views.APIView):

    def get(self, request, username):
        try:
            cliente = User.objects.get(username=username)
            
            ordenes = Orden.objects.filter(cliente=cliente).order_by('-fecha')
            
            serializer = OrdenSerializer(ordenes, many=True)
            return response.Response(serializer.data)

        except User.DoesNotExist:
            return response.Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)