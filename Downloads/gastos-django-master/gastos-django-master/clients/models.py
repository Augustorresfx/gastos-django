from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

class Aeronave(models.Model):
    title = models.CharField(max_length=100)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    expiration = models.DateField(blank=True, null=True)
    matricula = models.CharField(max_length=100, blank=True, null=True)
    horas_disponibles = models.FloatField(blank=True, null=True, default=0.0)
    horas_voladas = models.FloatField(blank=True, null=True, default=0.0)
    ciclos_motor = models.IntegerField(blank=True, null=True, default=0)
    vencimiento_anexo_2 = models.DateField(blank=True, null=True)
    vencimiento_inspeccion_anual = models.DateField(blank=True, null=True)
    vencimiento_notaciones_requerimiento = models.DateField(blank=True, null=True)
    horas_inspecciones_varias_25 = models.FloatField(blank=True, null=True, default=25.0)
    horas_inspecciones_varias_50 = models.FloatField(blank=True, null=True, default=50.0)
    horas_inspecciones_varias_100 = models.FloatField(blank=True, null=True, default=100.0)
    

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Aeronaves'
    def clean(self):
        if self.horas_disponibles < 0:
            raise ValidationError('Horas disponibles no pueden ser negativas.')
    def __str__(self):
        return self.title + '. Matrícula: ' + self.matricula

class Base(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Bases'
    def __str__(self):
        return self.title

class Rol(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Roles'
    def __str__(self):
        return self.title

class Otro(models.Model):
    name = models.CharField(max_length=100)
    expiration = models.DateField(blank=True, null=True)
    horas_voladas = models.FloatField(blank=True, null=True, default=0.0)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Otros'
    def __str__(self):
        return self.name + '. Rol: ' + self.rol.title

class Piloto(models.Model):
    name = models.CharField(max_length=100)
    expiration = models.DateField()
    horas_voladas = models.FloatField(blank=True, null=True, default=0.0)
    
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
    
class Iva(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    porcentaje = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Ivas'
        
    def __str__(self):
        return self.title
    
    def __float__(self):
        return self.porcentaje
    
class ImpuestoVario(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    porcentaje = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Impuestos varios'
        
    def __str__(self):
        return self.title
    
    def __float__(self):
        return self.porcentaje
    
class ConceptoNoGrabado(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    porcentaje = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Conceptos no grabados'
        
    def __str__(self):
        return self.title
    
    def __float__(self):
        return self.porcentaje
    
class Categoria(models.Model): 
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.title

class Traslado(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Traslados'

    def __str__(self):
        return self.title

class Moneda(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    representacion = models.CharField(max_length=30, blank=True, null=True)
    
    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Monedas'

    def __str__(self):
        return self.title
    
class Gasto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_gasto', blank=True, null=True)
    traslado = models.ForeignKey(Traslado, on_delete=models.CASCADE, null=True, blank=True)
    responsable = models.ForeignKey(User, related_name='responsable_gasto', on_delete=models.CASCADE, null=True, blank=True)
    base = models.ForeignKey(Base, on_delete=models.CASCADE, null=True, blank=True)
    aeronave = models.ForeignKey(Aeronave, on_delete=models.CASCADE, null=True, blank=True) 
    subtotal = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_compra = models.DateField(null=True, blank=True)
    numero_compra = models.IntegerField(null=True, blank=True)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE, null=True, blank=True)
    cuit = models.CharField(max_length=100, blank=True, null=True)
    concepto_no_grabado = models.ForeignKey(ConceptoNoGrabado, on_delete=models.CASCADE, blank=True, null=True)
    concepto_no_grabado_total = models.FloatField(null=True, blank=True)
    iva = models.ForeignKey(Iva, on_delete=models.CASCADE, blank=True, null=True)
    iva_total = models.FloatField(null=True, blank=True)
    impuesto_vario = models.ForeignKey(ImpuestoVario, on_delete=models.CASCADE, null=True, blank=True)
    impuesto_vario_total = models.FloatField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    
    
    class Meta:
        ordering = ('responsable', )
        verbose_name_plural = 'Gastos'

    def __str__(self):
        return self.responsable.username + 'Total: ' + str(self.total)
 
    def calcular_total(self):
       
        subtotal = self.subtotal

        iva = self.iva_total

        impuestos_varios = self.impuesto_vario_total

        concepto_no_grabado = self.concepto_no_grabado_total

        suma = subtotal + iva + impuestos_varios + concepto_no_grabado

        total = suma

        return total

    def save(self,*args,**kwargs):
        
        self.total = float(self.calcular_total())
        super().save(*args, **kwargs)


class Operacion(models.Model):
    aeronave = models.ForeignKey(Aeronave, related_name='operaciones', on_delete=models.CASCADE)
    pilot = models.ForeignKey(Piloto, related_name='operaciones', on_delete=models.CASCADE)
    title = models.ForeignKey(Base, related_name='operaciones', on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now, editable=True, blank=True)
    fecha = models.DateField(default=timezone.now)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alumn = models.ForeignKey(Otro, on_delete=models.CASCADE, null=True, blank=True)
    mechanic = models.ForeignKey(Mecanico, related_name='operaciones', on_delete=models.CASCADE, null=True, blank=True)
    fuel = models.IntegerField()
    used_fuel = models.IntegerField(blank=True, null=True)
    takeoff_place = models.CharField(max_length=100)
    landing_place = models.CharField(max_length=100)
    engine_ignition_1 = models.TimeField()

    takeoff_time = models.TimeField()
    landing_time = models.TimeField()
    engine_cut_1 = models.TimeField()

    cant_pasajeros = models.IntegerField(blank=True, null=True)
    

    total_encendido_1 = models.DurationField(blank=True, null=True)
    total_horas_aeronave = models.FloatField(blank=True, null=True, default=0.0)
    total_horas_disponibles_aeronave = models.FloatField(blank=True, null=True, default=0.0)
    total_horas_piloto = models.FloatField(blank=True, null=True, default=0.0)
    total_horas_alumn = models.FloatField(blank=True, null=True, default=0.0)
    total_ciclos_encendido = models.IntegerField(blank=True, null=True, default=0)
    number_of_landings = models.IntegerField()
    number_of_splashdowns = models.IntegerField(blank=True, null=True)
    start_up_cycles = models.IntegerField(blank=True, null=True)
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

    class Meta:
     
        verbose_name_plural = 'Operaciones'

    def __str__(self):
        return self.title.title + ', ID: ' + str(self.id)
    
    
    def calcular_combustible_usado(self):
       
        cargado = self.fuel

        remanente = self.fuel_on_landing

        restar = cargado - remanente


        used_fuel = restar

        return used_fuel
    
        # restar horas de vuelo a horas disponibles de aeronave

    def restar_horas_disponibles(self):
        if not self.pk: # Verificar si es una instancia recién creada
            # Convertir los horarios de despegue y aterrizaje a datetime con fecha ficticia (hoy)
            dt_despegue = datetime.combine(self.created, self.takeoff_time)
            dt_aterrizaje = datetime.combine(self.created, self.landing_time)

            # Si el horario de aterrizaje es anterior al horario de despegue, sumar 1 día a la fecha de aterrizaje
            if dt_despegue > dt_aterrizaje:
                dt_aterrizaje += timedelta(days=1)

            # Calcular la diferencia de tiempo en segundos y convertir a horas enteras
            segundos_de_vuelo = (dt_aterrizaje - dt_despegue).total_seconds()
            horas_de_vuelo = float(segundos_de_vuelo / 3600)

            # Restar las horas de vuelo a las horas disponibles de la aeronave
            
            self.aeronave.horas_disponibles -= round(horas_de_vuelo, 2)
            self.aeronave.horas_voladas += round(horas_de_vuelo, 2)
            self.aeronave.horas_inspecciones_varias_25 -= round(horas_de_vuelo, 2)
            self.aeronave.horas_inspecciones_varias_50 -= round(horas_de_vuelo, 2)
            self.aeronave.horas_inspecciones_varias_100 -= round(horas_de_vuelo, 2)
            self.pilot.horas_voladas += round(horas_de_vuelo, 2)
            if self.alumn:
                self.alumn.horas_voladas += round(horas_de_vuelo, 2)
                self.alumn.save()
                self.total_horas_alumn = self.alumn.horas_voladas

            # Sumar ciclos motor
            self.aeronave.ciclos_motor += self.start_up_cycles
            self.aeronave.save()
            self.pilot.save()
            self.total_ciclos_encendido = self.aeronave.ciclos_motor
            self.total_horas_aeronave = self.aeronave.horas_voladas
            self.total_horas_disponibles_aeronave = self.aeronave.horas_disponibles
            self.total_horas_piloto = self.pilot.horas_voladas



    def save(self,*args,**kwargs):
        if self.created is None:
            self.created = timezone.now()
        # Calcula el total de tiempo encendido de los motores
        if self.engine_cut_1 and self.engine_ignition_1:
            total_encendido_1 = datetime.combine(datetime.today(), self.engine_cut_1) - datetime.combine(datetime.today(), self.engine_ignition_1)
            self.total_encendido_1 = timedelta(hours=total_encendido_1.seconds // 3600, minutes=total_encendido_1.seconds // 60 % 60)
        
        # Guarda el combustible usado
        self.used_fuel = int(self.calcular_combustible_usado())
        super().save(*args, **kwargs)

# conectar el método a la señal pre_save
@receiver(pre_save, sender=Operacion)
def actualizar_horas_disponibles(sender, instance, **kwargs):
    instance.restar_horas_disponibles()