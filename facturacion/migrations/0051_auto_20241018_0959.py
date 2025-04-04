# Generated by Django 2.1.15 on 2024-10-18 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0020_auto_20241018_0854'),
        ('facturacion', '0050_auto_20241017_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liquidaciondetalle',
            name='usuarioCrea',
        ),
        migrations.AddField(
            model_name='liquidacion',
            name='totalAbonos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='liquidaciondetalle',
            name='tipoHonorario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TipoHonorario091', to='tarifas.TiposHonorarios'),
        ),
        migrations.AddField(
            model_name='liquidaciondetalle',
            name='tipoRegistro',
            field=models.CharField(blank=True, choices=[('M', 'MANUAL'), ('S', 'SISTEMA')], max_length=20, null=True),
        ),
    ]
