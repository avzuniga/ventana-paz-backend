from django.db import models


class VentanaModelQuerySet(models.QuerySet):
    def all(self):
        return self.filter(archived=False)

    def removed(self):
        return self.filter(archived=True)


class VentanaModelManager(models.Manager):
    def get_queryset(self):
        return VentanaModelQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().order_by('-id')

    def removed(self):
        return self.get_queryset().removed().order_by('-id')