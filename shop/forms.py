from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            '__all__'
        )
        
        widgets = {
      'description': forms.Textarea(attrs={'cols': 14, 'rows': 3}),
    }