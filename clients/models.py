from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

# Create your models here.

class Aeronave(models.Model):
    title = models.CharField(max_length=100)
    expiration = models.DateField()
    matricula = models.CharField(max_length=100)
    horas_disponibles = models.FloatField()
    horas_voladas = models.FloatField(blank=True, null=True, default=0)
    ciclos_motor = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Aeronaves'
    def clean(self):
        if self.horas_disponibles < 0:
            raise ValidationError('Horas disponibles no pueden ser negativas.')
    def __str__(self):
        return self.title

class Base(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Bases'
    def __str__(self):
        return self.title

class Piloto(models.Model):
    name = models.CharField(max_length=100)
    expiration = models.DateField()

    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Pilotos'
    def __str__(self):
        return self.name
    
class Mecanico(models.Model):
    name = models.CharField(max_length=100)
    expiration = models.DateField()
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Mecanicos'
    def __str__(self):
        return self.name

class Razon(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Motivos'
        
    def __str__(self):
        return self.title

class Operador(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Operadores'
        
    def __str__(self):
        return self.name
    
class Cliente(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Clientes'
        
    def __str__(self):
        return self.name
    
class Impuesto(models.Model):
    title = models.CharField(max_length=100)
    porcentaje = models.DecimalField(decimal_places=3, max_digits=6)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Impuestos'
        
    def __str__(self):
        return self.title
    
    def __float__(self):
        return self.porcentaje
    
class Categoria(models.Model): 
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.title

class Gasto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subtotal = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    emision = models.DateField()
    description = models.TextField(blank=True)
    cuit = models.CharField(max_length=100)
    rubro = models.CharField(max_length=100)
    impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=100, blank=True)
    
    
    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Gastos'

    def __str__(self):
        return self.title
 
    def calcular_total(self):
       
        subtotal = self.subtotal

        impuesto = self.impuesto.porcentaje

        sumar = subtotal * impuesto

        total = subtotal + sumar

        return total

    def save(self,*args,**kwargs):
        
        self.total = float(self.calcular_total())
        super().save(*args, **kwargs)


class Operacion(models.Model):
    aeronave = models.ForeignKey(Aeronave, related_name='operaciones', on_delete=models.CASCADE)
    pilot = models.ForeignKey(Piloto, related_name='operaciones', on_delete=models.CASCADE)
    title = models.ForeignKey(Base, related_name='operaciones', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alumn = models.CharField(max_length=100, blank=True)
    mechanic = models.ForeignKey(Mecanico, related_name='operaciones', on_delete=models.CASCADE)
    fuel = models.IntegerField()
    used_fuel = models.IntegerField(blank=True, null=True)
    takeoff_place = models.CharField(max_length=100)
    landing_place = models.CharField(max_length=100)
    engine_ignition_1 = models.TimeField()
    engine_ignition_2 = models.TimeField(blank=True, null=True)
    takeoff_time = models.TimeField()
    landing_time = models.TimeField()
    engine_cut_1 = models.TimeField()
    engine_cut_2 = models.TimeField(blank=True, null=True)
    total_encendido_1 = models.DurationField(blank=True, null=True)
    total_encendido_2 = models.DurationField(blank=True, null=True)
    number_of_landings = models.IntegerField()
    number_of_splashdowns = models.IntegerField(blank=True, null=True)
    start_up_cycles = models.IntegerField()
    fuel_on_landing = models.IntegerField()
    water_release_cycles = models.IntegerField(blank=True)
    water_release_amount = models.IntegerField(blank=True)
    cycles_with_external_load = models.IntegerField(blank=True)
    weight_with_external_load = models.IntegerField(blank=True)
    reason_of_flight = models.ForeignKey(Razon, related_name='operaciones', on_delete=models.CASCADE)
    other_reason = models.CharField(max_length=100, blank=True)
    operator = models.ForeignKey(Operador, related_name='operaciones', on_delete=models.CASCADE)
    client = models.ForeignKey(Cliente, related_name='operaciones', on_delete=models.CASCADE)
    operation_note = models.TextField(blank=True)
    maintenance_note = models.TextField(blank=True)

    def __str__(self):
         return self.title + "- by " + self.user.username
    
    
    def calcular_combustible_usado(self):
       
        cargado = self.fuel

        remanente = self.fuel_on_landing

        restar = cargado - remanente


        used_fuel = restar

        return used_fuel
    
        # restar horas de vuelo a horas disponibles de aeronave
    def restar_horas_disponibles(self):
        # Convertir los horarios de despegue y aterrizaje a datetime con fecha ficticia (hoy)
        dt_despegue = datetime.combine(datetime.today(), self.takeoff_time)
        dt_aterrizaje = datetime.combine(datetime.today(), self.landing_time)

        # Si el horario de aterrizaje es anterior al horario de despegue, sumar 1 día a la fecha de aterrizaje
        if dt_despegue > dt_aterrizaje:
            dt_aterrizaje += timedelta(days=1)

        # Calcular la diferencia de tiempo en segundos y convertir a horas enteras
        segundos_de_vuelo = (dt_aterrizaje - dt_despegue).total_seconds()
        horas_de_vuelo = float(segundos_de_vuelo / 3600)

        # Restar las horas de vuelo a las horas disponibles de la aeronave
        self.aeronave.horas_disponibles -= round(horas_de_vuelo, 2)
        self.aeronave.horas_voladas += round(horas_de_vuelo, 2)

        # Sumar ciclos motor
        self.aeronave.ciclos_motor += self.start_up_cycles
        self.aeronave.save()

    def save(self,*args,**kwargs):
        # Calcula el total de tiempo encendido de los motores
        if self.engine_cut_1 and self.engine_ignition_1:
            total_encendido_1 = datetime.combine(datetime.today(), self.engine_cut_1) - datetime.combine(datetime.today(), self.engine_ignition_1)
            self.total_encendido_1 = timedelta(hours=total_encendido_1.seconds // 3600, minutes=total_encendido_1.seconds // 60 % 60)
        if self.engine_cut_2 and self.engine_ignition_2:
            total_encendido_2 = datetime.combine(datetime.today(), self.engine_cut_2) - datetime.combine(datetime.today(), self.engine_ignition_2)
            self.total_encendido_2 = timedelta(hours=total_encendido_2.seconds // 3600, minutes=total_encendido_2.seconds // 60 % 60)
        # Guarda el combustible usado
        self.used_fuel = int(self.calcular_combustible_usado())
        super().save(*args, **kwargs)

# conectar el método a la señal pre_save
@receiver(pre_save, sender=Operacion)
def actualizar_horas_disponibles(sender, instance, **kwargs):
    instance.restar_horas_disponibles()