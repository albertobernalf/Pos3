# Generated by Django 2.1.15 on 2024-08-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacion', '0003_convenios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convenios',
            name='porcEsterilizacion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='convenios',
            name='porcMaterial',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='convenios',
            name='porcSuministros',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='convenios',
            name='porcTarifario',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='convenios',
            name='valorOxigeno',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
