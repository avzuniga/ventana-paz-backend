from datetime import datetime, timedelta
from . import models
from backend.apps.utils.serializers import CustomSerializer
from rest_framework import serializers


class PerfilSerializer(CustomSerializer):
    class Meta:
        model = models.Perfil
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]


class TiendaSerializer(CustomSerializer):
    productos_read = serializers.ReadOnlyField(source='get_products')

    class Meta:
        model = models.Tienda
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
            'productos_read'
        ]


class ElementoSerializer(CustomSerializer):
    tienda_read = serializers.ReadOnlyField(source='get_tienda')

    class Meta:
        model = models.Elemento
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
            'tienda_read'
        ]


class ImagenSerializer(CustomSerializer):
    class Meta:
        model = models.Imagen
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]
