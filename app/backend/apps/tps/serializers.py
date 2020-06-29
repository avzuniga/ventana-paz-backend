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
    
    class Meta:
        model = models.Tienda
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]

class ElementoSerializer(CustomSerializer):
    
    class Meta:
        model = models.Elemento
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]