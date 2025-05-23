# Generated by Django 2.1.15 on 2024-07-19 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20240710_1531'),
        ('planta', '0003_auto_20240702_1521'),
        ('enfermeria', '0008_notasliquidosenfermeria'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotasEnfermeria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consecAdmision', models.IntegerField(default=0)),
                ('folio', models.IntegerField(default=0)),
                ('tipoNota', models.CharField(max_length=3000)),
                ('nota', models.CharField(max_length=20000)),
                ('fecha', models.DateTimeField()),
                ('tipoEvento', models.CharField(max_length=2000)),
                ('descripcion', models.CharField(max_length=5000)),
                ('actividadPrevencion', models.CharField(max_length=5000)),
                ('notificacionevento', models.CharField(max_length=500)),
                ('selloCalidad', models.CharField(max_length=5)),
                ('grupoSanguineo', models.CharField(max_length=100)),
                ('fechaVencimiento', models.DateTimeField()),
                ('accesoVenoso', models.CharField(max_length=2000)),
                ('volumenHemocomponente', models.CharField(max_length=5000)),
                ('signosVitales', models.CharField(max_length=5000)),
                ('acompañamientoMedico', models.CharField(max_length=5000)),
                ('tripulacionAmbulancia', models.CharField(max_length=2000)),
                ('movil', models.CharField(max_length=3000)),
                ('auxiliarEncargado', models.CharField(max_length=100)),
                ('traslado', models.CharField(max_length=500)),
                ('estadoPaciente', models.CharField(max_length=1000)),
                ('soporte', models.CharField(max_length=500)),
                ('estadoPiel', models.CharField(max_length=5000)),
                ('entregaDocumentos', models.CharField(max_length=5000)),
                ('duracionMasaje', models.CharField(max_length=500)),
                ('codigoHuella', models.CharField(max_length=100)),
                ('epicrisis', models.CharField(max_length=5000)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('acompañante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.UsuariosContacto')),
                ('documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoHistoria111', to='usuarios.Usuarios')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento')),
                ('turno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='enfermeria.TurnosEnfermeria')),
                ('usuarioRegistro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
    ]
