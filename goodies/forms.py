from .models import product, catergory
from django.forms import ModelForm

class catergoryform():
	class meta:
		model = catergory
		fields = '__all__'

class productform(ModelForm):
	class meta:
		model = product
		fields ='__all__'

