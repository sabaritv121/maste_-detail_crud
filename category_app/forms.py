from django import forms
from category_app.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category','product_name')