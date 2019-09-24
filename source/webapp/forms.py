from django import forms
from webapp.models import PRODUCT_CATEGORY_CHOICES

class SearchForm(forms.Form):
    search_name = forms.CharField(max_length=300, label='Имя', required=True)


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название', required=True)
    description = forms.CharField(max_length=2000, label='Описание', required=True)
    category = forms.ChoiceField(label='Категория', choices=PRODUCT_CATEGORY_CHOICES,required=True)
    amount = forms.IntegerField(label='Остаток', min_value= 0,required=True)
    price = forms.DecimalField(max_digits=7, min_value=0, decimal_places=2, label='Цена',required=True)