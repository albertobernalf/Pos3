# Generated by Django 2.1.15 on 2025-03-31 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0117_auto_20250325_1233'),
        ('tarifarios', '0004_auto_20250331_1122'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tarifariosprocedimientos',
            unique_together={('tiposTarifa', 'codigoCups')},
        ),
    ]
