from .models import product, catergory
from django.forms import ModelForm
from .models import product
from sale.models import Sale
from django import forms

class catergoryform(ModelForm):
	class Meta:
		model = catergory
		fields = '__all__'

class productform(ModelForm):
	class Meta:
		model = product
		fields ='__all__'

class DateForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()

class AddProduct(forms.Form):
    add_quantity = forms.IntegerField()
