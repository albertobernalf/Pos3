# Generated by Django 2.1.15 on 2025-02-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rips', '0033_ripstransaccion_numfactura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ripshospitalizacion',
            name='ripsTipos',
        ),
        migrations.AddField(
            model_name='ripshospitalizacion',
            name='tipoRips',
            field=models.CharField(default='FACTURA', editable=False, max_length=10),
        ),
    ]
