# Generated by Django 2.1.15 on 2025-03-12 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rips', '0041_auto_20250304_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ripsurgenciasobservacion',
            name='itemFactura',
        ),
    ]
