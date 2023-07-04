from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['quantite']
        widgets = {
            'quantite': forms.NumberInput(attrs={'min': 1}),
        }