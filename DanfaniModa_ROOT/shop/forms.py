from django import forms
from .models import Produit
# from .models import Order


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model=Order
#         fields=['quantite']
#         widgets = {
#             'quantite': forms.NumberInput(attrs={'min': 1}),
#         }


    

class ProductForm(forms.ModelForm):
    class Meta:
        model=Produit
        fields=('titre','prix','description','categorie','image','similaire','type')
        widgets={
            'titre':forms.TextInput(attrs={'style':'width:300px; height:20px;padding:5px;margin:10px;'}),
            'prix':forms.NumberInput(attrs={'style':'width:300px; height:20px;padding:5px;margin:10px'}),
            'categorie':forms.Select(attrs={'style':'width:300px; height:30px;padding:5px;margin:10px'}),
            'image':forms.FileInput(attrs={'style':'width:300px; height:30px;padding:5px;margin:10px'}),
            'description':forms.Textarea(attrs={'style':'width:300px; height:150px;padding:5px;margin:10px'}),
            'similaire':forms.TextInput(attrs={'style':'width:300px; height:20px;padding:5px;margin:10px'}),
            'type':forms.TextInput(attrs={'style':'width:300px; height:20px;padding:5px;margin:10px'}),
        }
        label_attrs={
            'titre':{'class':'control-title'}
        }

        required_css_class = 'hidden'