# Generated by Django 4.1.2 on 2023-04-09 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_aeronave_horas_voladas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aeronave',
            name='ciclos_motor',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
