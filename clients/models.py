from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
    
class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Mechanics'
    def __str__(self):
        return self.name

class Reason(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Reasons'
        
    def __str__(self):
        return self.title

class Operator(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Operators'
        
    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Clients'
        
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alumn = models.CharField(max_length=100, blank=True)
    mechanic = models.ForeignKey(Mechanic, related_name='products', on_delete=models.CASCADE)
    fuel = models.IntegerField(max_length=50)
    takeoff_place = models.CharField(max_length=100)
    landing_place = models.CharField(max_length=100)
    engine_ignition_1 = models.TimeField()
    engine_ignition_2 = models.TimeField()
    takeoff_time = models.TimeField()
    landing_time = models.TimeField()
    engine_cut_1 = models.TimeField()
    engine_cut_2 = models.TimeField()
    number_of_landings = models.IntegerField(max_length=100)
    number_of_splashdowns = models.IntegerField(max_length=100)
    start_up_cycles = models.IntegerField(max_length=100)
    fuel_on_landing = models.IntegerField(max_length=100)
    fuel_per_flight = models.IntegerField(max_length=100)
    water_release_cycles = models.IntegerField(max_length=100)
    water_release_amount = models.IntegerField(max_length=100)
    cycles_with_external_load = models.IntegerField(max_length=100)
    weight_with_external_load = models.IntegerField(max_length=100)
    reason_of_flight = models.ForeignKey(Reason, related_name='products', on_delete=models.CASCADE)
    other_reason = models.CharField(max_length=100, blank=True)
    operator = models.ForeignKey(Operator, related_name='products', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='products', on_delete=models.CASCADE)
    loaded_fuel = models.IntegerField(max_length=100)
    operation_note = models.TextField(blank=True)
    maintenance_note = models.TextField(blank=True)
    def __str__(self):
         return self.title + "- by " + self.user.username