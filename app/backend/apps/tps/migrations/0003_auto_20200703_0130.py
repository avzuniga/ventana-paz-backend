# Generated by Django 2.2 on 2020-07-03 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tps', '0002_auto_20200703_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tienda',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
