# Generated by Django 2.1.15 on 2024-07-19 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0003_auto_20240702_1521'),
        ('usuarios', '0003_auto_20240710_1531'),
        ('enfermeria', '0003_cuidadosenfermeria'),
    ]

    operations = [
        migrations.CreateModel(
            name='DolorEnfermeria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consecAdmision', models.IntegerField(default=0)),
                ('folio', models.IntegerField(default=0)),
                ('fechaCreacion', models.DateTimeField()),
                ('zona', models.CharField(max_length=3000)),
                ('dolorPorcentaje', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dolorDescripcion', models.CharField(max_length=100)),
                ('lateralidad', models.CharField(max_length=100)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoHistoria2121', to='usuarios.Usuarios')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento')),
                ('turno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='enfermeria.TurnosEnfermeria')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
    ]
