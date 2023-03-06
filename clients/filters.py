import django_filters
from django_filters import DateFromToRangeFilter
from .models import Product, Gasto
from .forms import forms

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['title', 'category', 'pilot', 'alumn', 'mechanic', 'fuel', 'takeoff_place', 
                  'landing_place', 'engine_ignition_1', 'engine_ignition_2', 'takeoff_time', 'landing_time', 
                  'engine_cut_1', 'engine_cut_2', 'number_of_landings', 'number_of_splashdowns', 'start_up_cycles', 'fuel_on_landing', 
                  'fuel_per_flight', 'water_release_cycles', 'water_release_amount', 'cycles_with_external_load', 
                  'weight_with_external_load', 'reason_of_flight', 'other_reason', 'operator', 'client', 'loaded_fuel', 'operation_note', 'maintenance_note'
                  ]
        widgets = {
            'pilot': forms.Select(attrs={
                'class': 'form-select'
            }),
            'operator': forms.Select(attrs={
                'class': 'form-select'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'start_up_cycles': forms.Select(attrs={
                'class': 'form-select'
            })

        }

class GastosFilter(django_filters.FilterSet):
    class Meta:
        model = Gasto
        fields = ['title', 'price', 'description']