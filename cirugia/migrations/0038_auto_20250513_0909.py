# Generated by Django 2.1.15 on 2025-05-13 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0037_auto_20250513_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cirugias',
            name='tipofractura',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
