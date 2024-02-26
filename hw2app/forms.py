from django import forms
from .models import ProductModel

class ProductForms(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'description', 'price', 'count', 'photo',]


