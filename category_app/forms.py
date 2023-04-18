from django import forms
from category_app.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category','product_name')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
        }