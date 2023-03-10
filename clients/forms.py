from django.forms import ModelForm
from django import forms

from .models import Operacion, Aeronave, Gasto

class ClientFilterForm(ModelForm):
    class Meta:
        model = Operacion
        fields = [
            'title',
        ]

class GastoForm(ModelForm):
    class Meta:
        model = Gasto
        fields = ['title', 'subtotal', 'description', 'emision', 'cuit', 'rubro', 'categoria', 'impuesto']
        widgets = {
            'impuesto': forms.Select(attrs={
                'class': 'form-select'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class ClientForm(ModelForm):
    class Meta:
        model = Operacion
        fields = ['title', 'aeronave', 'pilot', 'alumn', 'mechanic', 'fuel', 'takeoff_place', 
                  'landing_place', 'engine_ignition_1', 'engine_ignition_2', 'takeoff_time', 'landing_time', 
                  'engine_cut_1', 'engine_cut_2', 'number_of_landings', 'number_of_splashdowns', 'start_up_cycles', 'fuel_on_landing', 
                  'fuel_per_flight', 'water_release_cycles', 'water_release_amount', 'cycles_with_external_load', 
                  'weight_with_external_load', 'reason_of_flight', 'other_reason', 'operator', 'client', 'operation_note', 'maintenance_note'
                  ]
        widgets = {
            'aeronave': forms.Select(attrs={
                'class': 'form-select'
            }),
            'pilot': forms.Select(attrs={
                'class': 'form-select'
            }),
            'mechanic': forms.Select(attrs={
                'class': 'form-select'
            }),
            'reason_of_flight': forms.Select(attrs={
                'class': 'form-select'
            }),
            'operator': forms.Select(attrs={
                'class': 'form-select'
            }),
            'client': forms.Select(attrs={
                'class': 'form-select'
            })
        }
