# Generated by Django 4.1.2 on 2023-05-16 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0017_alter_operacion_cant_pasajeros'),
    ]

    operations = [
        migrations.AddField(
            model_name='aeronave',
            name='aterrizajes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='operacion',
            name='total_aterrizajes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='operacion',
            name='fuel_on_landing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='operacion',
            name='number_of_landings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]