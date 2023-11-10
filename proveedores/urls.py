from rest_framework import routers
from .api import ProveedorViewSet

router = routers.DefaultRouter()

router.register('api/proveedores', ProveedorViewSet, 'proveedores')

urlpatterns = router.urls
