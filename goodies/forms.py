from .models import product, catergory
from django.forms import ModelForm
from .models import product
from sale.models import Sale
from django import forms

class catergoryform():
	class meta:
		model = catergory
		fields = '__all__'

class productform(ModelForm):
	class meta:
		model = product
		fields ='__all__'

class DateForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
