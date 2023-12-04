from django.db.models import Sum, F
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

    def create(self, request, *args, **kwargs):
        username = request.query_params.get('username')
        if 'orden' not in request.data or not request.data['orden']:
            user = self.get_user_by_username(username) if username else None
            if not user:
                return response.Response({'error': 'User not found or username is required'}, status=status.HTTP_400_BAD_REQUEST)
            request.data['orden'] = self.create_orden(user).id

        resp = super(OrdenItemViewSet, self).create(request, *args, **kwargs)
        self.update_orden_precio_total(resp.data['orden'])
        return resp

    def update(self, request, *args, **kwargs):
        resp = super(OrdenItemViewSet, self).update(request, *args, **kwargs)
        orden_item = self.get_object()

        # Update Orden's total price
        self.update_orden_precio_total(orden_item.orden.id)

        # Check and update Orden's estado if necessary
        if orden_item.estado != 0:
            self.check_and_update_orden_estado(orden_item.orden)

        return resp

    def update_orden_precio_total(self, orden_id):
        total_price = OrdenItem.objects.filter(orden_id=orden_id).annotate(
            item_total=F('cantidad') * F('producto__precio')
        ).aggregate(total=Sum('item_total'))['total'] or 0
        Orden.objects.filter(id=orden_id).update(precio_total=total_price)

    def check_and_update_orden_estado(self, orden):
        orden_items = OrdenItem.objects.filter(orden=orden)
        if not orden_items.filter(estado=0).exists():
            Orden.objects.filter(id=orden.id).update(estado=4)

    def update_orden_precio_total(self, orden_id):
        total_price = OrdenItem.objects.filter(orden_id=orden_id).annotate(
            item_total=F('cantidad') * F('producto__precio')
        ).aggregate(total=Sum('item_total'))['total'] or 0
        Orden.objects.filter(id=orden_id).update(precio_total=total_price)

    def get_user_by_username(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def create_orden(self, user):
        new_orden = Orden(cliente=user)
        new_orden.save()
        return new_orden

class GetOrdenView(views.APIView):

    def get(self, request, username):
        try:
            cliente = User.objects.get(username=username)
        except User.DoesNotExist:
            return response.Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        latest = request.query_params.get('latest', 'false').lower() == 'true'
        ordenes = Orden.objects.filter(cliente=cliente).order_by('-fecha')
        orden = ordenes.first() if latest and ordenes.exists() else None

        if latest and not orden:
            return response.Response({'message': 'No orders found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrdenSerializer(orden if latest else ordenes, many=not latest)
        return response.Response(serializer.data)

class GetItemsOrdenView(views.APIView):

    def get(self, request):
        orden_id = request.query_params.get('orden_id')
        if not orden_id:
            return response.Response({'error': 'Orden ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        if not Orden.objects.filter(id=orden_id).exists():
            return response.Response({'error': 'Orden not found'}, status=status.HTTP_404_NOT_FOUND)

        orden_items = OrdenItem.objects.filter(orden_id=orden_id)
        serializer = OrdenItemSerializer(orden_items, many=True)

        return response.Response(serializer.data)

class GetOrdenItemsByRestauranteProveedorView(views.APIView):

    def get(self, request):
        restaurante_id = request.query_params.get('restaurante')
        proveedor_id = request.query_params.get('proveedor')

        if restaurante_id:
            orden_items = self.get_orden_items_by_restaurante(restaurante_id)
        elif proveedor_id:
            orden_items = self.get_orden_items_by_proveedor(proveedor_id)
        else:
            return response.Response({'error': 'Restaurante or Proveedor ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = OrdenItemSerializer(orden_items, many=True)
        return response.Response(serializer.data)

    def get_orden_items_by_restaurante(self, restaurante_id):
        try:
            restaurante_id = int(restaurante_id)
            return OrdenItem.objects.filter(producto__restaurantes__id=restaurante_id)
        except ValueError:
            return OrdenItem.objects.none()

    def get_orden_items_by_proveedor(self, proveedor_id):
        try:
            proveedor_id = int(proveedor_id)
            return OrdenItem.objects.filter(producto__proveedores__id=proveedor_id)
        except ValueError:
            return OrdenItem.objects.none()
