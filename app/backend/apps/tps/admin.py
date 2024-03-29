from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'correo',
        'contraseña',
        'nombre',
        'edad',
        'tienda',
        'cuenta'
    ]
    search_fields = [
        'correo',
        'tienda',
        'nombre',
        'id'
    ]

    list_filter = [
        'edad'
    ]


@admin.register(models.Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'indicativo',
        'whatsapp',
        'ubicacion',
        'imagen'
    ]
    search_fields = [
        'nombre',
        'id'
    ]

    list_filter = [
        'indicativo'
    ]


@admin.register(models.Elemento)
class ElementoAdmin(admin.ModelAdmin):
    filter_horizontal = ('imagenes', )
    list_display = [
        'id',
        'titulo',
        'descripcion',
        'precio',
        'tienda'
    ]
    search_fields = [
        'titulo',
        'id'
    ]

    list_filter = [
        'tienda',
        'precio'
    ]


@admin.register(models.Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'imagen',
    ]
    search_fields = [
        'id'
    ]

    list_filter = [
    ]