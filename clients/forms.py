from django.forms import ModelForm
from django import forms
from .models import Operacion, Aeronave, Gasto, Piloto, Mecanico, Otro

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
        
class ClientFilterForm(ModelForm):
    class Meta:
        model = Operacion
        fields = [
            'title',
        ]

class OtroForm(ModelForm):
    class Meta:
        model = Otro
        fields = ['name', 'expiration', 'horas_voladas', 'rol']
        widgets = {
            'rol': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class GastoForm(ModelForm):
    class Meta:
        model = Gasto
        fields = ['base', 'aeronave', 'traslado', 'responsable', 'categoria', 'fecha_compra', 'numero_compra', 'cuit', 'moneda', 'subtotal', 'concepto_no_grabado', 'concepto_no_grabado_total', 'iva', 'iva_total', 'impuesto_vario', 'impuesto_vario_total' ]
        widgets = {
            'iva': forms.Select(attrs={
                'class': 'form-select'
            }),
            'concepto_no_grabado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'impuesto_vario': forms.Select(attrs={
                'class': 'form-select'
            }),
            'base': forms.Select(attrs={
                'class': 'form-select'
            }),
            'aeronave': forms.Select(attrs={
                'class': 'form-select'
            }),
            'traslado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'responsable': forms.Select(attrs={
                'class': 'form-select'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class ClientForm(ModelForm):
    class Meta:
        model = Operacion
        fields = ['title', 'aeronave', 'pilot', 'alumn', 'mechanic', 'fecha', 'cant_pasajeros', 'fuel', 'takeoff_place', 
                  'landing_place', 'engine_ignition_1', 'takeoff_time', 'landing_time', 
                  'engine_cut_1', 'number_of_landings', 'number_of_splashdowns', 'start_up_cycles', 'fuel_on_landing',
                    'water_release_cycles', 'water_release_amount', 'cycles_with_external_load', 
                  'weight_with_external_load', 'reason_of_flight', 'other_reason', 'operator', 'client', 'operation_note', 'maintenance_note'
                  ]
        widgets = {
            'title': forms.Select(attrs={
                'class': 'form-select'
            }),
            'aeronave': forms.Select(attrs={
                'class': 'form-select'
            }),
            'pilot': forms.Select(attrs={
                'class': 'form-select'
            }),
            'mechanic': forms.Select(attrs={
                'class': 'form-select'
            }),
            'alumn': forms.Select(attrs={
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
        widgets['alumn'].required = False  # Make 'alumn' optional
class AeronaveForm(ModelForm):
    class Meta:
        model = Aeronave
        fields = ['title', 'matricula', 'horas_disponibles', 'horas_voladas', 'ciclos_motor', 'expiration', 'vencimiento_anexo_2', 'vencimiento_inspeccion_anual', 'vencimiento_notaciones_requerimiento', 'horas_inspecciones_varias_25', 'horas_inspecciones_varias_50', 'horas_inspecciones_varias_100']

class PilotoForm(ModelForm):
    class Meta:
        model = Piloto
        fields = ['name', 'expiration', 'horas_voladas']

class MecanicoForm(ModelForm):
    class Meta:
        model = Mecanico
        fields = ['name', 'expiration']
        