import django_filters
from django_filters import DateFromToRangeFilter
from .models import Product, Gasto
from .forms import forms


class ProductFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.filters['title'].label = 'Titulo'
        self.filters['category'].label = 'Aeronave'
        self.filters['pilot'].label = 'Piloto'
        self.filters['operator'].label = 'Operador'
        self.filters['mechanic'].label = 'Mecánico'


    class Meta:
        model = Product
        
        fields = [ 'title', 'category', 'pilot', 'operator', 'mechanic'
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

def __init__(self, *args, **kwargs):
    super(ProductFilter, self).__init__(*args, **kwargs)
    self.filters['title'].label="Titulo"

class GastosFilter(django_filters.FilterSet):
    class Meta:
        model = Gasto
        fields = ['title', 'price', 'description']