# Generated by Django 2.1.15 on 2025-02-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0111_auto_20250224_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiamedicamentos',
            name='concentracionMedicamento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
