# Generated by Django 2.1.15 on 2025-05-07 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0121_auto_20250502_1619'),
        ('cirugia', '0022_cirugias_tiposcirugia'),
    ]

    operations = [
        migrations.AddField(
            model_name='cirugiasparticipantes',
            name='medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TipoHonorario12', to='clinico.EspecialidadesMedicos'),
        ),
    ]
