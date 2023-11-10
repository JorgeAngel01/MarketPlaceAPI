from rest_framework import routers
from .api import RestauranteViewSet

router = routers.DefaultRouter()

router.register('api/restaurantes', RestauranteViewSet, 'restaurantes')

urlpatterns = router.urls
