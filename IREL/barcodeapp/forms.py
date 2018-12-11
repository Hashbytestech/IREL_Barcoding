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
        model=ShelfSticker
        fields="__all__"

class ProductstickerForm(ModelForm):
    class Meta:
        model=ProductSticker
        fields=['product_code',]
#
class ExitForm(ModelForm):
    class Meta:
        model=Exit
        fields='__all__'

class InspectionForm(ModelForm):
    class Meta:
        model=Inspection
        fields='__all__'

#
# class ProductFilter(django_filters.FilterSet):
#     class Meta:
#         model = Product
#         fields =['product_code','name',]