# Generated by Django 2.1.15 on 2025-02-07 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0058_auto_20241126_1550'),
        ('rips', '0011_auto_20250204_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ripsenvios',
            name='numeroEnvio',
        ),
        migrations.AddField(
            model_name='ripsenvios',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='empre12', to='facturacion.Empresas'),
        ),
    ]
