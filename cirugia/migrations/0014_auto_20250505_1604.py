# Generated by Django 2.1.15 on 2025-05-05 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0013_auto_20250505_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programacioncirugias',
            old_name='sedesClinica_id',
            new_name='sedesClinica',
        ),
    ]
