# Generated by Django 4.1.2 on 2023-03-16 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aeronave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('expiration', models.DateField()),
                ('matricula', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Aeronaves',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('porcentaje', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Impuestos',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expiration', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Mecanicos',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Operadores',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expiration', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Pilotos',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Razon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Razones',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('alumn', models.CharField(blank=True, max_length=100)),
                ('fuel', models.IntegerField()),
                ('takeoff_place', models.CharField(max_length=100)),
                ('landing_place', models.CharField(max_length=100)),
                ('engine_ignition_1', models.TimeField()),
                ('engine_ignition_2', models.TimeField()),
                ('takeoff_time', models.TimeField()),
                ('landing_time', models.TimeField()),
                ('engine_cut_1', models.TimeField()),
                ('engine_cut_2', models.TimeField()),
                ('number_of_landings', models.IntegerField()),
                ('number_of_splashdowns', models.IntegerField(blank=True)),
                ('start_up_cycles', models.IntegerField()),
                ('fuel_on_landing', models.IntegerField()),
                ('fuel_per_flight', models.IntegerField()),
                ('water_release_cycles', models.IntegerField(blank=True)),
                ('water_release_amount', models.IntegerField(blank=True)),
                ('cycles_with_external_load', models.IntegerField(blank=True)),
                ('weight_with_external_load', models.IntegerField(blank=True)),
                ('other_reason', models.CharField(blank=True, max_length=100)),
                ('operation_note', models.TextField(blank=True)),
                ('maintenance_note', models.TextField(blank=True)),
                ('aeronave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operaciones', to='clients.aeronave')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operaciones', to='clients.cliente')),
                ('mechanic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operaciones', to='clients.mecanico')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operaciones', to='clients.operador')),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operaciones', to='clients.piloto')),
                ('reason_of_flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operaciones', to='clients.razon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtotal', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('emision', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('cuit', models.CharField(max_length=100)),
                ('rubro', models.CharField(max_length=100)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.categoria')),
                ('impuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.impuesto')),
            ],
            options={
                'verbose_name_plural': 'Gastos',
                'ordering': ('title',),
            },
        ),
    ]
