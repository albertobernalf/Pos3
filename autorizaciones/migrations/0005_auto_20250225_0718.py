# Generated by Django 2.1.15 on 2025-02-25 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0065_auto_20250225_0717'),
        ('sitios', '0014_sedesclinica_codigohabilitacion'),
        ('clinico', '0113_auto_20250225_0717'),
        ('usuarios', '0007_tiposdocumento_tipodocrips'),
        ('planta', '0005_planta_correo'),
        ('autorizaciones', '0004_auto_20250225_0717'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AutorizacionesCups',
            new_name='AutorizacionesDetalle',
        ),
    ]
