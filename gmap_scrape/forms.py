from django import forms

class DollarForm(forms.Form):
    dollar = forms.CharField( label='米ドル', max_length=50,required=True,)