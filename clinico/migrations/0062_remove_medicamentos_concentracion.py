# Generated by Django 2.1.15 on 2024-09-11 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0061_auto_20240911_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamentos',
            name='concentracion',
        ),
    ]
