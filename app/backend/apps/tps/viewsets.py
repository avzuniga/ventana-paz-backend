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

    @action(detail=False, methods=['get'])
    def get_perfil(self, request):
        user = request.user
        perfil = get_object_or_none(models.Perfil, cuenta=user)
        if perfil:
            serializer = serializers.PerfilSerializer(perfil)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'status': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class TiendaViewSet(viewsets.ModelViewSet):
    queryset = models.Tienda.objects.all()
    serializer_class = serializers.TiendaSerializer
    model = models.Tienda

    def get_queryset(self):
        param = self.request.query_params.get('param', None)
        if param == 'visitas':
            tiendas = models.Tienda.objects.all().order_by('-visitas', '-id')
        elif param == 'recientes':
            tiendas = models.Tienda.objects.all().order_by('-id')
        else:
            tiendas = models.Tienda.objects.all()
        return tiendas

    @action(detail=True, methods=['get'])
    def visit(self, request, pk=None):
        tienda = get_object_or_none(models.Tienda, id=pk)
        if tienda:
            tienda.visitas = tienda.visitas + 1
            tienda.save()
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        return Response({'status': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def filter_tienda(self, request):
        words = request.query_params.get('words', None)
        if words:
            tiendas = models.Tienda.objects.filter(nombre__icontains=words).order_by('-visitas', '-id')
            serializer = serializers.TiendaSerializer(tiendas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def filter_by_product(self, request):
        words = request.query_params.get('words', None)
        tiendas = []
        data = []
        if words:
            productos = models.Elemento.objects.filter(titulo__icontains=words).order_by('-tienda__visitas',
                                                                                         '-tienda__id')
            for producto in productos:
                if producto.tienda in tiendas:
                    continue
                tiendas.append(producto.tienda)
            for tienda in tiendas:
                data.append(serializers.TiendaSerializer(tienda).data)
            return Response(data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def filter_by_product_just(self, request):
        words = request.query_params.get('words', None)
        data = []
        if words:
            productos = models.Elemento.objects.filter(titulo__icontains=words).order_by('-tienda__visitas',
                                                                                         '-tienda__id')
            for producto in productos:
                data.append(serializers.ElementoSerializer(producto).data)
            return Response(data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)


class ElementoViewSet(viewsets.ModelViewSet):
    queryset = models.Elemento.objects.all()
    serializer_class = serializers.ElementoSerializer
    model = models.Elemento


class ImagenViewSet(viewsets.ModelViewSet):
    queryset = models.Imagen.objects.all()
    serializer_class = serializers.ImagenSerializer
    model = models.Imagen
