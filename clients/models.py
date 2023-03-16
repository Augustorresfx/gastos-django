from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Aeronave(models.Model):
    title = models.CharField(max_length=100)
    expiration = models.DateField()
    matricula = models.CharField(max_length=100)
    

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Aeronaves'
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
        verbose_name_plural = 'Razones'
        
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

        print(self.impuesto.__float__)

        total = subtotal + sumar

        return total

    def save(self,*args,**kwargs):
        # are you really sure that you want to save a string ???
        self.total = float(self.calcular_total())
        super().save(*args, **kwargs)


class Operacion(models.Model):
    aeronave = models.ForeignKey(Aeronave, related_name='operaciones', on_delete=models.CASCADE)
    pilot = models.ForeignKey(Piloto, related_name='operaciones', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alumn = models.CharField(max_length=100, blank=True)
    mechanic = models.ForeignKey(Mecanico, related_name='operaciones', on_delete=models.CASCADE)
    fuel = models.IntegerField()
    takeoff_place = models.CharField(max_length=100)
    landing_place = models.CharField(max_length=100)
    engine_ignition_1 = models.TimeField()
    engine_ignition_2 = models.TimeField()
    takeoff_time = models.TimeField()
    landing_time = models.TimeField()
    engine_cut_1 = models.TimeField()
    engine_cut_2 = models.TimeField()
    number_of_landings = models.IntegerField()
    number_of_splashdowns = models.IntegerField(blank=True)
    start_up_cycles = models.IntegerField()
    fuel_on_landing = models.IntegerField()
    fuel_per_flight = models.IntegerField()
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