from .models import Review
from .serializers import ReviewSerializer
from django.contrib.auth.models import User
# from restaurantes.models import Restaurante
# from proveedores.models import Proveedor
# from productos.models import Producto
from rest_framework import viewsets, permissions, response, status, views

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ReviewSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        review = serializer.instance
        if review.restaurante:
            all_reviews = Review.objects.filter(restaurante=review.restaurante)
            total_rating = sum(r.calificacion for r in all_reviews)
            average_rating = total_rating / all_reviews.count()
            restaurante = review.restaurante
            restaurante.promedio_calific = average_rating
            restaurante.save()
            print(f"Promedio Restaurante Guardado: {average_rating}")
        elif review.proveedor:
            all_reviews = Review.objects.filter(proveedor=review.proveedor)
            total_rating = sum(r.calificacion for r in all_reviews)
            average_rating = total_rating / all_reviews.count()
            proveedor = review.proveedor
            proveedor.promedio_calific = average_rating
            proveedor.save()
            print(f"Promedio Proveedor Guardado: {average_rating}")
        elif review.producto:
            all_reviews = Review.objects.filter(producto=review.producto)
            total_rating = sum(r.calificacion for r in all_reviews)
            average_rating = total_rating / all_reviews.count()
            producto = review.producto
            producto.promedio_calific = average_rating
            producto.save()
            print(f"Promedio Producto Guardado: {average_rating}")

        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class GetReviewView(views.APIView):

    def get(self, request):
        username = request.query_params.get('username')
        restaurante = request.query_params.get('restaurante')
        proveedor = request.query_params.get('proveedor')
        producto = request.query_params.get('producto')

        if username:
            try:
                autor = User.objects.get(username=username)
            except User.DoesNotExist:
                return response.Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            reviews = Review.objects.filter(autor=autor)
        elif restaurante:
            reviews = Review.objects.filter(restaurante=restaurante)
        elif proveedor:
            reviews = Review.objects.filter(proveedor=proveedor)
        elif producto:
            reviews = Review.objects.filter(producto=producto)
        else:
            return response.Response({'error': 'No username or restaurante provided'}, status=status.HTTP_400_BAD_REQUEST)
                
        if not reviews.exists():
            return response.Response({'error': 'No reviews found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(reviews, many=True)
        return response.Response(serializer.data)
