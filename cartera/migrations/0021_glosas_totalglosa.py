# Generated by Django 2.1.15 on 2025-04-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartera', '0020_pagos_convenio'),
    ]

    operations = [
        migrations.AddField(
            model_name='glosas',
            name='totalGlosa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
