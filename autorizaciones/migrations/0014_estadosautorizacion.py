# Generated by Django 2.1.15 on 2025-02-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autorizaciones', '0013_autorizacionesdetalle_tiposuministro'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadosAutorizacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
    ]
