# Generated by Django 2.1.15 on 2025-02-07 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0013_auto_20241115_1218'),
        ('rips', '0012_auto_20250207_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='ripsenvios',
            name='sedesClinica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='SedesClinica759', to='sitios.SedesClinica'),
        ),
    ]
