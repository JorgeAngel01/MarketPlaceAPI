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
            if username:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    return response.Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return response.Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
            new_orden = Orden(cliente=user)
            new_orden.save()
            request.data['orden'] = new_orden.id

        # return super(OrdenItemViewSet, self).create(request, *args, **kwargs)
        response = super(OrdenItemViewSet, self).create(request, *args, **kwargs)
        self.update_orden_precio_total(response.data['orden'])
        return response
    
    def update(self, request, *args, **kwargs):
        # Existing logic for updating an OrdenItem...
        response = super(OrdenItemViewSet, self).update(request, *args, **kwargs)
        self.update_orden_precio_total(response.data['orden'])
        return response

    def update_orden_precio_total(self, orden_id):
        orden = Orden.objects.get(id=orden_id)
        total_price = OrdenItem.objects.filter(orden=orden).annotate(
            item_total=F('cantidad') * F('producto__precio')
        ).aggregate(Sum('item_total'))['item_total__sum'] or 0
        orden.precio_total = total_price
        orden.save()

class GetOrdenView(views.APIView):

    def get(self, request, username):
        try:
            cliente = User.objects.get(username=username)
            
            latest = request.query_params.get('latest', 'false').lower() == 'true'

            if latest:
                orden = Orden.objects.filter(cliente=cliente).order_by('-fecha').first()
                if orden:
                    serializer = OrdenSerializer(orden)
                else:
                    return response.Response({'message': 'No orders found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                ordenes = Orden.objects.filter(cliente=cliente).order_by('-fecha')
                serializer = OrdenSerializer(ordenes, many=True)

            return response.Response(serializer.data)

        except User.DoesNotExist:
            return response.Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
