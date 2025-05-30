# Generated by Django 2.1.15 on 2025-05-15 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0010_remove_planta_serviciosadministrativos'),
        ('tarifarios', '0010_auto_20250502_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='GruposQx',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MinimosLegalesQx',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('año', models.CharField(blank=True, max_length=4, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='TablaHonorarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('homologado', models.CharField(default='A', editable=False, max_length=8)),
                ('smldv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('grupoQx', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifarios.GruposQx')),
                ('tiposHonorarios', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifarios.TiposHonorarios')),
                ('tiposTarifaProducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifarios.TiposTarifaProducto')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
        migrations.CreateModel(
            name='TablaMaterialSuturaCuracion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('homologado', models.CharField(default='A', editable=False, max_length=8)),
                ('smldv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cruento', models.CharField(blank=True, editable=False, max_length=1, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('grupoQx', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifarios.GruposQx')),
                ('tiposTarifaProducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifarios.TiposTarifaProducto')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
        migrations.CreateModel(
            name='TablaSalasDeCirugia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('homologado', models.CharField(default='A', editable=False, max_length=8)),
                ('smldv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cruento', models.CharField(blank=True, editable=False, max_length=1, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('grupoQx', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifarios.GruposQx')),
                ('tiposTarifaProducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifarios.TiposTarifaProducto')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
    ]
