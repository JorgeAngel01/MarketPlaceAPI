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
from usuarios.api import UsuarioViewSet, RegistroAPIView, LogoutAPIView
from restaurantes.api import RestauranteViewSet
from proveedores.api import ProveedorViewSet
from productos.api import ProductoViewSet
from ordenes.api import OrdenViewSet, OrdenItemViewSet
from reviews.api import ReviewViewSet



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
]
