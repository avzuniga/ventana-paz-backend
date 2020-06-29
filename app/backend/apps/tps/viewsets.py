from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from backend.apps.utils.shortcuts import get_object_or_none
from . import models, serializers


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = models.Perfil.objects.all()
    serializer_class = serializers.PerfilSerializer
    model = models.Perfil


class TiendaViewSet(viewsets.ModelViewSet):
    queryset = models.Tienda.objects.all()
    serializer_class = serializers.TiendaSerializer
    model = models.Tienda


class ElementoViewSet(viewsets.ModelViewSet):
    queryset = models.Elemento.objects.all()
    serializer_class = serializers.ElementoSerializer
    model = models.Elemento