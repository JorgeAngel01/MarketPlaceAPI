from .models import Restaurante
from django.contrib.auth.models import User
from .serializers import RestauranteSerializer
from rest_framework import viewsets, permissions, views, response, status

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RestauranteSerializer

class GetRestaurantView(views.APIView):

    def get(self, request, username):
        try:
            propietario = User.objects.get(username=username)
            
            restaurantes = Restaurante.objects.filter(propietario=propietario)
            
            serializer = RestauranteSerializer(restaurantes, many=True)
            return response.Response(serializer.data)

        except User.DoesNotExist:
            return response.Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)