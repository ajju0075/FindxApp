from django import forms
from products import models as products_models



class ProductsForm(forms.ModelForm):
    class Meta:
        model = products_models.ProductsModel
        fields = ["category", "product_name", "price", "description", "image",]