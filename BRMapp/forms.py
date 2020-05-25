from django import forms


class NewBookForms(forms.Form):
    title = forms.CharField(label='Title', max_length=60)
    price = forms.FloatField(label='Price')
    author = forms.CharField(label='Author')
    publisher = forms.CharField(label='Publisher')


class SearchForm(forms.Form):
    title = forms.CharField(label='Title', max_length=60)

