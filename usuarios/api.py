from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views, permissions, generics, response, status
from rest_framework.authtoken.models import Token
from .serializers import UsuarioSerializer, RegistroSerializer
from restaurantes.models import Restaurante
from proveedores.models import Proveedor

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegistroAPIView(generics.CreateAPIView):
    serializer_class = RegistroSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # We create a token than will be used for future auth
        token = Token.objects.create(user=serializer.instance)
        token_data = {"token": token.key}
        return response.Response(
            {**serializer.data, **token_data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class LogoutAPIView(views.APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return response.Response(status=status.HTTP_200_OK)

class GetUserByNameView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            user_data = {
                'user_id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
            if Restaurante.objects.filter(propietario=user).exists():
                user_data['tipo'] = 'restaurante'
            elif Proveedor.objects.filter(propietario=user).exists():
                user_data['tipo'] = 'proveedor'
            else:
                user_data['tipo'] = 'nothing'
            return response.Response(user_data)
        except User.DoesNotExist:
            return response.Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
