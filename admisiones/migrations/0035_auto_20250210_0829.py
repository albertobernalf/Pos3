# Generated by Django 2.1.15 on 2025-02-10 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admisiones', '0034_ingresos_ripsdestinousuarioegresoreciennacido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresos',
            name='salidaMotivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='salidaMotivo01', to='clinico.TiposSalidas'),
        ),
    ]
