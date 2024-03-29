# Generated by Django 4.1.2 on 2023-05-12 23:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_remove_operacion_engine_cut_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacion',
            name='cant_pasajeros',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='operacion',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='operacion',
            name='start_up_cycles',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
