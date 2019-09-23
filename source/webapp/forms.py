from django import forms

class SearchForm(forms.Form):
    search_name = forms.CharField(max_length=300, label='Имя', required=True)