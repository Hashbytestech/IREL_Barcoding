from .models import *
from django.forms import ModelForm
import django_filters

class StockForm(ModelForm):
    class Meta:
        model=Stock
        fields='__all__'

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"

class ShelfstickerForm(ModelForm):
    class Meta:
        model=Shelfsticker
        fields="__all__"

class ProductstickerForm(ModelForm):
    class Meta:
        model=Productsticker
        fields=['product_code',]

#
#
# class ProductFilter(django_filters.FilterSet):
#     class Meta:
#         model = Product
#         fields =['product_code','name',]