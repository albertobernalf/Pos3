# Generated by Django 2.1.15 on 2025-01-30 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0005_planta_correo'),
        ('clinico', '0104_auto_20250130_0807'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='medicos',
            unique_together={('planta',)},
        ),
    ]
