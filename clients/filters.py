import django_filters
from django_filters import DateFromToRangeFilter, RangeFilter
from .models import Operacion, Gasto
from .forms import forms, PeopleFilterFormHelper
from django_filters.widgets import RangeWidget
from django_range_slider.fields import RangeSliderField
from .custom_filter import CustomRangeWidget


class AllRangeFilter(RangeFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        values = [p.fuel for p in Operacion.objects.all()]
        min_value = min(values)
        max_value = max(values)
        self.extra['widget'] = CustomRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})

class WaterReleaseCyclesRange(RangeFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        values = [p.water_release_cycles for p in Operacion.objects.all()]
        min_value = min(values)
        max_value = max(values)
        self.extra['widget'] = CustomRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})



class FuelFilter(django_filters.FilterSet):
    fuel = AllRangeFilter()

    class Meta:
        model = Operacion
        fields = ['fuel']
        form = PeopleFilterFormHelper


class WaterAmountRange(RangeFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        values = [p.water_release_amount for p in Operacion.objects.all()]
        min_value = min(values)
        max_value = max(values)
        self.extra['widget'] = CustomRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})



class ProductFilter(django_filters.FilterSet):
    fuel = AllRangeFilter()
    water_release_cycles = WaterReleaseCyclesRange()
    water_release_amount = WaterAmountRange()
    created = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'AÑO/MES/DIA'}))

    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.filters['fuel'].label = 'Combustible'
        self.filters['title'].label = 'Titulo'
        self.filters['aeronave'].label = 'Aeronave'
        self.filters['pilot'].label = 'Piloto'
        self.filters['water_release_cycles'].label = 'Ciclos de lanzamiento de agua'
        self.filters['operator'].label = 'Operador'
        self.filters['created'].label = 'Fecha de creación'
        self.filters['mechanic'].label = 'Mecánico'



    class Meta:
        model = Operacion

        fields = [ 'title', 'aeronave', 'fuel', 'pilot', 'operator', 'mechanic', 'water_release_cycles', 'water_release_amount', 'created'
                  ]
        form = PeopleFilterFormHelper
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