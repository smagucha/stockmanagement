from .models import Product, Catergory
from django.forms import ModelForm
from sale.models import Sale
from django import forms

class catergoryform(ModelForm):
	class Meta:
		model = Catergory
		fields = '__all__'

class productform(ModelForm):
	class Meta:
		model = Product
		fields ='__all__'

class DateForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()

class AddProduct(forms.Form):
    add_quantity = forms.IntegerField()
