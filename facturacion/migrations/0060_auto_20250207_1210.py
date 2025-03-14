# Generated by Django 2.1.15 on 2025-02-07 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rips', '0015_auto_20250207_1036'),
        ('facturacion', '0059_auto_20250207_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturacion',
            name='motivoGlosa',
        ),
        migrations.RemoveField(
            model_name='facturacion',
            name='numeroglosa',
        ),
        migrations.RemoveField(
            model_name='facturacion',
            name='totalCantidadAceptada',
        ),
        migrations.RemoveField(
            model_name='facturacion',
            name='totalCantidadGlosada',
        ),
        migrations.RemoveField(
            model_name='facturacion',
            name='totalCantidadSoportado',
        ),
        migrations.AddField(
            model_name='facturacion',
            name='ripsEnvio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rips.RipsEnvios'),
        ),
    ]
