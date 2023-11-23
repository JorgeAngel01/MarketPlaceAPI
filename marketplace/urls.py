"""
URL configuration for marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from usuarios.api import UsuarioViewSet, RegistroAPIView, LogoutAPIView, GetUserByNameView
from restaurantes.api import RestauranteViewSet, GetRestaurantView, CatRestauranteListView
from proveedores.api import ProveedorViewSet, GetProveedorView, CatProveedorListView
from productos.api import ProductoViewSet, GetProductosRestauranteView, GetProductosProveedorView, CatProductoListView, EstProductoPListView
from ordenes.api import OrdenViewSet, OrdenItemViewSet, GetOrdenView
from reviews.api import ReviewViewSet, GetReviewView



router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'restaurantes', RestauranteViewSet)
router.register(r'ordenes', OrdenViewSet)
router.register(r'items_ordenes', OrdenItemViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('registro/', RegistroAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('login/', obtain_auth_token),
    path('usuario/<str:username>', GetUserByNameView.as_view()),
    path('restaurante/<str:username>', GetRestaurantView.as_view()),
    path('restaurantes/categorias', CatRestauranteListView.as_view()),
    path('proveedor/<str:username>', GetProveedorView.as_view()),
    path('proveedores/categorias', CatProveedorListView.as_view()),
    path('reviews/<str:username>', GetReviewView.as_view()),
    path('ordenes/<str:username>', GetOrdenView.as_view()),
    path('productos_restaurante/<int:restaurante_id>', GetProductosRestauranteView.as_view()),
    path('productos_proveedor/<int:proveedor_id>', GetProductosProveedorView.as_view()),
    path('productos/categorias', CatProductoListView.as_view()),
    path('productos/estados', EstProductoPListView.as_view()),
]
