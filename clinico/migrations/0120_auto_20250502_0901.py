# Generated by Django 2.1.15 on 2025-05-02 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0017_auto_20250502_0713'),
        ('clinico', '0119_auto_20250501_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historia',
            name='dependenciasRealizado',
        ),
        migrations.AddField(
            model_name='historia',
            name='serviciosAdministrativos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='seradm50', to='sitios.ServiciosAdministrativos'),
        ),
    ]
