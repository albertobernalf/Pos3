# Generated by Django 2.1.15 on 2024-10-23 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0030_auto_20241022_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarifassuministros',
            name='concepto',
        ),
    ]
