import django_filters
from django_filters import DateFromToRangeFilter, RangeFilter
from .models import Operacion, Gasto
from .forms import forms
from django_filters.widgets import RangeWidget



class ProductFilter(django_filters.FilterSet):
    fuel = RangeFilter()
    water_release_cycles = RangeFilter()
    water_release_amount = RangeFilter()
    created = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'AÑO/MES/DIA'}))

    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.filters['fuel'].label = 'Combustible'
        self.filters['title'].label = 'Titulo'
        self.filters['aeronave'].label = 'Aeronave'
        self.filters['pilot'].label = 'Piloto'
        self.filters['client'].label = 'Cliente'
        self.filters['water_release_cycles'].label = 'Ciclos de lanzamiento de agua'
        self.filters['water_release_amount'].label = 'Cantidad de agua lanzada'
        self.filters['operator'].label = 'Operador'
        self.filters['created'].label = 'Fecha de creación'
        self.filters['mechanic'].label = 'Mecánico'
        self.filters['reason_of_flight'].label = 'Motivo del vuelo'



    class Meta:
        model = Operacion

        fields = [ 'title', 'aeronave', 'fuel', 'pilot', 'operator', 'mechanic', 'client', 'water_release_cycles', 'water_release_amount', 'created', 'reason_of_flight'
                  ]
        widgets = {
  
            'pilot': forms.Select(attrs={
                'class': 'form-select'
            }),
            'operator': forms.Select(attrs={
                'class': 'form-select'
            }),
            'aeronave': forms.Select(attrs={
                'class': 'form-select'
            }),
            'client': forms.Select(attrs={
                'class': 'form-select'
            }),
            'start_up_cycles': forms.Select(attrs={
                'class': 'form-select'
            }),
            'reason_of_flight': forms.Select(attrs={
                'class': 'form-select'
            })

        }
   

def __init__(self, *args, **kwargs):
    super(ProductFilter, self).__init__(*args, **kwargs)
    self.filters['title'].label="Titulo"

class GastosFilter(django_filters.FilterSet):
    class Meta:
        model = Gasto
        fields = ['title', 'total', 'description']