from django.forms import ModelForm
from django import forms

from .models import Product, Category

class ClientForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }
