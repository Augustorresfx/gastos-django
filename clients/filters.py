import django_filters
from django_filters import DateFromToRangeFilter, RangeFilter
from .models import Operacion, Gasto
from .forms import forms
from django_filters.widgets import RangeWidget
from django_range_slider.fields import RangeSliderField

class ProductFilter(django_filters.FilterSet):
    fuel = RangeFilter(widget=RangeWidget(attrs={'type': 'range', 'step': '0.01', 'min': '0', 'max': '1000'}))
    water_release_cycles = RangeFilter()
    water_release_amount = RangeFilter()
    created = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))

    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.filters['title'].label = 'Titulo'
        self.filters['aeronave'].label = 'Aeronave'
        self.filters['pilot'].label = 'Piloto'
        self.filters['operator'].label = 'Operador'
        self.filters['mechanic'].label = 'Mecánico'



    class Meta:
        model = Operacion

        fields = [ 'title', 'aeronave', 'pilot', 'operator', 'mechanic', 'fuel', 'water_release_cycles', 'water_release_amount', 'created'
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
            'start_up_cycles': forms.Select(attrs={
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