# Generated by Django 2.1.15 on 2025-02-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rips', '0037_auto_20250224_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ripsmedicamentos',
            name='cantidadMedicamento',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True),
        ),
    ]
