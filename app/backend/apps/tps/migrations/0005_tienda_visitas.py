# Generated by Django 2.2 on 2020-08-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tps', '0004_auto_20200805_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='visitas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
