# Generated by Django 4.1.2 on 2023-04-14 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_alter_operacion_alumn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacion',
            name='alumn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.otro'),
        ),
    ]
