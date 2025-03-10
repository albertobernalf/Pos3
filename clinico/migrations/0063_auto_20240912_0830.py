# Generated by Django 2.1.15 on 2024-09-12 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20240911_0806'),
        ('planta', '0003_auto_20240702_1521'),
        ('clinico', '0062_remove_medicamentos_concentracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaMedicamentos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orden', models.IntegerField(default=0)),
                ('dosisCantidad', models.DecimalField(decimal_places=3, max_digits=20)),
                ('nota', models.CharField(blank=True, max_length=5000)),
                ('cantidadSolicitada', models.DecimalField(decimal_places=0, max_digits=20)),
                ('cantidadEntregada', models.DecimalField(decimal_places=0, max_digits=20)),
                ('cantidadDispensada', models.DecimalField(decimal_places=0, max_digits=20)),
                ('cantidadAplicada', models.DecimalField(decimal_places=0, max_digits=20)),
                ('cantidadDevuelta', models.DecimalField(decimal_places=0, max_digits=20)),
                ('cantidadfacturada', models.DecimalField(decimal_places=0, max_digits=20)),
                ('nopos', models.CharField(blank=True, max_length=1, null=True)),
                ('estadoMedicamento', models.CharField(blank=True, max_length=1, null=True)),
                ('horarioDosis', models.CharField(blank=True, max_length=200, null=True)),
                ('dosisUnica', models.DecimalField(decimal_places=0, max_digits=10)),
                ('dosisRescate', models.CharField(blank=True, max_length=200, null=True)),
                ('dosisProfilaxis', models.CharField(blank=True, max_length=200, null=True)),
                ('dosisAdelanto', models.CharField(blank=True, max_length=200, null=True)),
                ('urgente', models.CharField(blank=True, max_length=1, null=True)),
                ('dosificacion', models.CharField(blank=True, max_length=2000, null=True)),
                ('antibiotico', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaSuspension', models.DateTimeField()),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('dosisUnidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.UnidadesDeMedidaDosis')),
                ('frecuencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.FrecuenciasAplicacion')),
                ('historia', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoHistoriaDiag12', to='clinico.Historia')),
                ('suministro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='facturacion.Suministros')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
                ('viaAdministracion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.ViasAdministracion')),
            ],
        ),
        migrations.CreateModel(
            name='PrincipiosActivos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='antibiotico',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='cantidadAplicada',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='cantidadDevuelta',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='cantidadDispensada',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='cantidadEntregada',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='cantidadSaldoIni',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='cantidadSolicitada',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='cantidadfacturada',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='cantidadsaldoFinal',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='dosificacion',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='dosisAdelanto',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='dosisCantidad',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='dosisProfilaxis',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='dosisRescate',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='dosisUnica',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='dosisUnidad',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='estadoMedicamento',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='estadoReg',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='fechaRegistro',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='fechaSuspension',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='frecuenciaCantidad',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='frecuenciaUnidad',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='historia',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='horarioDosis',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='nopos',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='nota',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='orden',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='suministro',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='urgente',
        ),
        migrations.RemoveField(
            model_name='medicamentos',
            name='usuarioRegistro',
        ),
        migrations.AddField(
            model_name='medicamentos',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
