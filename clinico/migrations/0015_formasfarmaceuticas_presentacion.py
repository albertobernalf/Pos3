# Generated by Django 2.1.15 on 2024-07-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0014_unidadesdemedida_viasadministracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormasFarmaceuticas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigoMipres', models.DecimalField(decimal_places=0, max_digits=5)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('habilitadoMipres', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigoMipres', models.DecimalField(decimal_places=0, max_digits=5)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('habilitadoMipres', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaRegistro', models.DateTimeField(blank=True, null=True)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
    ]
