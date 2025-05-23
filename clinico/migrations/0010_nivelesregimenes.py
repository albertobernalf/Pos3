# Generated by Django 2.1.15 on 2024-07-09 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0009_auto_20240709_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='NivelesRegimenes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('porCuotaModeradora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('porCopago', models.DecimalField(decimal_places=2, max_digits=5)),
                ('porTopeEve', models.DecimalField(decimal_places=2, max_digits=5)),
                ('porTopeAnual', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estadoReg', models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='A', editable=False, max_length=1)),
                ('regimen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinico.Regimenes')),
            ],
        ),
    ]
