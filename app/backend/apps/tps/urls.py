
from django.urls import path, include
from rest_framework import routers
from . import viewsets
 
router = routers.DefaultRouter()
router.register(r'perfiles', viewsets.PerfilViewSet)
router.register(r'tiendas', viewsets.TiendaViewSet)
router.register(r'elementos', viewsets.ElementoViewSet)


urlpatterns = [
    path(r'', include(router.urls))
]