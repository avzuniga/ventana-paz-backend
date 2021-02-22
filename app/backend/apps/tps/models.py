from django.db import models
from backend.apps.utils.models import ModelBase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group, Permission


class Perfil(ModelBase):
    contraseña = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )
    nombre = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )
    correo = models.EmailField(
        blank=True,
        null=True
    )
    edad = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    tienda = models.ForeignKey(
        'tps.Tienda',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    cuenta = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True
    )

    def clean(self):
        if self.pk is None and self.contraseña is None:
            raise ValidationError({'contraseña': 'Debes ingresar una contraseña para los nuevos usuarios'})

    # sobre escribimos el evento de save para que cuando se cree un nuevo
    # ProfesionalSalud se cree el usuario de django correspondiente.
    def save(self, *args, **kwargs):
        # si el pk es nulo es un objeto nuevo y debemos crear el usuario
        # y los permisos respectivos de acuerdo a su perfil
        u = None
        if self.pk is None:
            u = User.objects.create_user(self.correo, None, self.contraseña)
            self.cuenta = u
            self.contraseña = ""  # no queremos guardar la contraseña como texto plano.
        # de lo contrario solo actualizamos la informacion en el usuario existente.
        else:
            u = self.cuenta
            u.username = self.correo
            u.first_name = self.nombre

        # deberiamos cambiar la contraseña?
        if (self.contraseña is not None and len(self.contraseña) > 5):
            u.set_password(self.contraseña)
            self.contraseña = ""

        u.save()
        super(Perfil, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'


class Tienda(ModelBase):
    nombre = models.CharField(
        max_length=45,
        blank=True,
        null=True
    )
    indicativo = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    whatsapp = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )
    ubicacion = models.CharField(
        max_length=45,
        blank=True,
        null=True
    )
    elementos = models.ManyToManyField(
        'tps.Elemento',
        blank=True,
        related_name='+'
    )
    descripcion = models.TextField(
        blank=True,
        null=True
    )
    visitas = models.PositiveIntegerField(
        default=0
    )
    imagen = models.FileField(
        upload_to='images',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.id)

    def get_products(self):
        from backend.apps.tps.serializers import ElementoSerializer
        return ElementoSerializer(Elemento.objects.filter(tienda_id=self.id), many=True).data

    class Meta:
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'


class Imagen(ModelBase):
    imagen = models.FileField(
        upload_to='images'
    )

    def __str__(self):
        return str(self.id)


class Elemento(ModelBase):
    titulo = models.CharField(
        max_length=45,
        blank=True,
        null=True
    )
    descripcion = models.TextField(
        blank=True,
        null=True
    )
    precio = models.FloatField(
        blank=True,
        null=True
    )

    tienda = models.ForeignKey(
        Tienda,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    imagenes = models.ManyToManyField(
        Imagen,
        blank=True
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'
