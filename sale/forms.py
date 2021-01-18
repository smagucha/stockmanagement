from django.forms import ModelForm
from .models import Sale

class saleform(ModelForm):
	class meta:
		model = Sale
		fields ='__all__'
