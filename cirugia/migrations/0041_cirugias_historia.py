# Generated by Django 2.1.15 on 2025-05-15 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0121_auto_20250502_1619'),
        ('cirugia', '0040_cirugias_sala'),
    ]

    operations = [
        migrations.AddField(
            model_name='cirugias',
            name='historia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Historia127', to='clinico.Historia'),
        ),
    ]
