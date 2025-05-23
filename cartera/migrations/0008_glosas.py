# Generated by Django 2.1.15 on 2024-09-27 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0003_auto_20240702_1521'),
        ('contratacion', '0006_auto_20240917_0902'),
        ('cartera', '0007_tiposnotas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glosas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaGlosa', models.DateTimeField(blank=True, null=True)),
                ('numeroGlosa', models.CharField(blank=True, max_length=20, null=True)),
                ('detalladaParcial', models.CharField(blank=True, max_length=1, null=True)),
                ('detalladaTotal', models.CharField(blank=True, max_length=1, null=True)),
                ('totalGlosa', models.DecimalField(decimal_places=2, max_digits=15)),
                ('totalSoportado', models.DecimalField(decimal_places=2, max_digits=15)),
                ('totalAceptado', models.DecimalField(decimal_places=2, max_digits=15)),
                ('observacones', models.CharField(blank=True, max_length=120, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
                ('convenio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contratacion.Convenios')),
                ('usuarioRegistro', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.Planta')),
            ],
        ),
    ]
