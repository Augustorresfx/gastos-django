from django.forms import ModelForm
from django import forms

from .models import Operacion, Aeronave, Gasto
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Field, Layout
from django import forms
from django_filters.fields import RangeField

class PeopleFilterFormHelper(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'get'
        layout_fields = []
        for field_name, field in self.fields.items():
            if isinstance(field, RangeField):
                layout_field = Field(field_name, template="forms/fields/range-slider.html")
            else:
                layout_field = Field(field_name)
            layout_fields.append(layout_field)
        layout_fields.append(StrictButton("Filtrar", name='submit', type='submit', css_class='btn btn-outline-primary btn-block mt-1'))
        self.helper.layout = Layout(*layout_fields)
        
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
