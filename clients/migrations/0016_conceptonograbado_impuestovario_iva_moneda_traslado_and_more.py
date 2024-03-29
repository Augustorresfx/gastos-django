# Generated by Django 4.1.2 on 2023-05-15 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0015_aeronave_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConceptoNoGrabado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('porcentaje', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
            ],
            options={
                'verbose_name_plural': 'Conceptos no grabados',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ImpuestoVario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('porcentaje', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
            ],
            options={
                'verbose_name_plural': 'Impuestos varios',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Iva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('porcentaje', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
            ],
            options={
                'verbose_name_plural': 'Ivas',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('representacion', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Monedas',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Traslado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Traslados',
                'ordering': ('title',),
            },
        ),
        migrations.AlterModelOptions(
            name='gasto',
            options={'ordering': ('responsable',), 'verbose_name_plural': 'Gastos'},
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='description',
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='emision',
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='impuesto',
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='rubro',
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='title',
        ),
        migrations.AddField(
            model_name='gasto',
            name='aeronave',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.aeronave'),
        ),
        migrations.AddField(
            model_name='gasto',
            name='base',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.base'),
        ),
        migrations.AddField(
            model_name='gasto',
            name='concepto_no_grabado_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gasto',
            name='fecha_compra',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gasto',
            name='impuesto_vario_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gasto',
            name='iva_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gasto',
            name='numero_compra',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gasto',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsable_gasto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aeronave',
            name='expiration',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aeronave',
            name='matricula',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.categoria'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='cuit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='subtotal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_gasto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Impuesto',
        ),
        migrations.AddField(
            model_name='gasto',
            name='concepto_no_grabado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.conceptonograbado'),
        ),
        migrations.AddField(
            model_name='gasto',
            name='impuesto_vario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.impuestovario'),
        ),
        migrations.AddField(
            model_name='gasto',
            name='iva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.iva'),
        ),
        migrations.AddField(
            model_name='gasto',
            name='moneda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.moneda'),
        ),
        migrations.AddField(
            model_name='gasto',
            name='traslado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.traslado'),
        ),
    ]
