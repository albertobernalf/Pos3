# Generated by Django 2.1.15 on 2024-10-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0011_liquidacionhonorarios_valoriss'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquidacionhonorarios',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
