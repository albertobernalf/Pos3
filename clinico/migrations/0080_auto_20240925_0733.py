# Generated by Django 2.1.15 on 2024-09-25 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinico', '0079_examenesrasgos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historiaexamenes',
            old_name='fechaPreliminar1',
            new_name='fechaInterpretacion1',
        ),
        migrations.RenameField(
            model_name='historiaexamenes',
            old_name='fechaPreliminar2',
            new_name='fechaInterpretacion2',
        ),
        migrations.RenameField(
            model_name='historiaexamenes',
            old_name='fechaPreliminar3',
            new_name='fechaInterpretacion3',
        ),
        migrations.RemoveField(
            model_name='historiaexamenes',
            name='preliminar1',
        ),
        migrations.RemoveField(
            model_name='historiaexamenes',
            name='preliminar2',
        ),
        migrations.RemoveField(
            model_name='historiaexamenes',
            name='preliminar3',
        ),
        migrations.RemoveField(
            model_name='historiaexamenes',
            name='resultado',
        ),
    ]
