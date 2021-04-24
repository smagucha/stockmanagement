from django.forms import ModelForm
from django import forms
from .models import Sale


class saleform(ModelForm):
	class Meta:
		model = Sale
		fields ='__all__'

class DateForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
