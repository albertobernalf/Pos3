# Generated by Django 2.1.15 on 2025-03-17 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartera', '0018_remove_estadosglosas_codigo'),
        ('rips', '0048_auto_20250317_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ripsotrosservicios',
            old_name='Glosa',
            new_name='glosa',
        ),
        migrations.AddField(
            model_name='ripsconsultas',
            name='cantidadAceptada',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsconsultas',
            name='cantidadGlosada',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsconsultas',
            name='cantidadSoportado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsconsultas',
            name='motivoGlosa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Glosa02', to='cartera.MotivosGlosas'),
        ),
        migrations.AddField(
            model_name='ripsconsultas',
            name='notasCreditoGlosa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsconsultas',
            name='notasCreditoOtras',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsconsultas',
            name='notasDebito',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsconsultas',
            name='vAceptado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsconsultas',
            name='valorGlosado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsconsultas',
            name='valorSoportado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsotrosservicios',
            name='cantidadAceptada',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsotrosservicios',
            name='cantidadGlosada',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsotrosservicios',
            name='cantidadSoportado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsotrosservicios',
            name='motivoGlosa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Glosa07', to='cartera.MotivosGlosas'),
        ),
        migrations.AddField(
            model_name='ripsotrosservicios',
            name='notasCreditoGlosa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsotrosservicios',
            name='notasCreditoOtras',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsotrosservicios',
            name='notasDebito',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsotrosservicios',
            name='vAceptado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsotrosservicios',
            name='valorGlosado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='ripsotrosservicios',
            name='valorSoportado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
