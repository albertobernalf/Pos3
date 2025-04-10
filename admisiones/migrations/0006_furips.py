# Generated by Django 2.1.15 on 2024-07-09 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicas', '0002_periodos'),
        ('clinico', '0008_hallazgos'),
        ('sitios', '0008_auto_20240708_0910'),
        ('planta', '0003_auto_20240702_1521'),
        ('usuarios', '0002_auto_20240708_0909'),
        ('admisiones', '0005_triage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furips',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consec', models.IntegerField()),
                ('numeroFactura', models.CharField(default='', max_length=20)),
                ('fechaRadicado', models.DateTimeField(blank=True, null=True)),
                ('direccionVictima', models.CharField(default='', max_length=80)),
                ('telVictima', models.CharField(default='', max_length=10)),
                ('eventoDescripcion', models.CharField(default='', max_length=500)),
                ('direccionEvento', models.CharField(default='', max_length=80)),
                ('fechaEvento', models.DateTimeField(blank=True, null=True)),
                ('estadoAsegurado', models.CharField(default='', max_length=20)),
                ('tipoVehiculo', models.CharField(default='', max_length=20)),
                ('placaAsegurado', models.CharField(default='', max_length=10)),
                ('marcaAsegurado', models.CharField(default='', max_length=15)),
                ('codigoaseguradora', models.CharField(default='', max_length=20)),
                ('poliza', models.CharField(default='', max_length=20)),
                ('fechaIniPoliza', models.DateTimeField(blank=True, null=True)),
                ('fechaFinPoliza', models.DateTimeField(blank=True, null=True)),
                ('documentoPlaca2', models.CharField(default='', max_length=20)),
                ('placa2', models.CharField(default='', max_length=10)),
                ('documentoPlaca3', models.CharField(default='', max_length=20)),
                ('placa3', models.CharField(default='', max_length=10)),
                ('documentoPropietario', models.CharField(default='', max_length=20)),
                ('nombresPropietario', models.CharField(default='', max_length=30)),
                ('apellidosPropietario', models.CharField(default='', max_length=30)),
                ('direccionProietario', models.CharField(default='', max_length=80)),
                ('telefonoPropietario', models.CharField(default='', max_length=20)),
                ('documentoConductor', models.CharField(default='', max_length=20)),
                ('nombresConductor', models.CharField(default='', max_length=30)),
                ('apellidosConductor', models.CharField(default='', max_length=30)),
                ('direccionConductor', models.CharField(default='', max_length=80)),
                ('telefonoConductor', models.CharField(default='', max_length=20)),
                ('completo', models.CharField(choices=[('S', 'S'), ('N', 'N')], default='A', editable=False, max_length=1)),
                ('tipoAutomotor', models.CharField(default='', max_length=20)),
                ('accidenteMultiple', models.CharField(choices=[('S', 'S'), ('N', 'N')], default='A', editable=False, max_length=1)),
                ('ingresoUci', models.CharField(choices=[('S', 'S'), ('N', 'N')], default='A', editable=False, max_length=1)),
                ('velocidadAutomotor', models.CharField(default='', max_length=50)),
                ('dispositivoSeguridad', models.CharField(default='', max_length=50)),
                ('tipoColision', models.CharField(default='', max_length=20)),
                ('radicadoSiras', models.CharField(default='', max_length=20)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], default='A', editable=False, max_length=1)),
                ('documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Documento4', to='usuarios.Usuarios')),
                ('documentoProfesional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
                ('dxPrincEgreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dx4', to='clinico.Diagnosticos')),
                ('dxPrincIngreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dx1', to='clinico.Diagnosticos')),
                ('dxRel1Egreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dx5', to='clinico.Diagnosticos')),
                ('dxRel1Ingreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dx2', to='clinico.Diagnosticos')),
                ('dxRel2Egreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dx6', to='clinico.Diagnosticos')),
                ('dxRel2Ingreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dx3', to='clinico.Diagnosticos')),
                ('evento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='basicas.Eventos')),
                ('localidadEvento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.Localidades')),
                ('municipioEvento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='muni2', to='sitios.Municipios')),
                ('municipioPropietario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='muni1', to='sitios.Municipios')),
                ('municipioconductor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.Municipios')),
                ('sedesClinica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='SedesClinica3', to='sitios.SedesClinica')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.TiposDocumento')),
                ('tipoDocConductor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipoDoc6', to='usuarios.TiposDocumento')),
                ('tipoDocPlaca2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipoDoc14', to='usuarios.TiposDocumento')),
                ('tipoDocPlaca3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipoDoc24', to='usuarios.TiposDocumento')),
                ('tipoDocProfesional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipoDoc5', to='usuarios.TiposDocumento')),
                ('tipoDocPropietario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipoDoc4', to='usuarios.TiposDocumento')),
                ('usuarioCrea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='planta1', to='planta.Planta')),
            ],
        ),
    ]
