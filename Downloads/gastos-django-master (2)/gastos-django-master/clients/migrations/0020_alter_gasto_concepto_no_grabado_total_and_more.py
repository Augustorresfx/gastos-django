# Generated by Django 4.1.2 on 2023-06-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0019_alter_aeronave_horas_disponibles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='concepto_no_grabado_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='impuesto_vario_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='iva_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
