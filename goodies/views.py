from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import product, catergory
from django.urls import reverse_lazy
from django.views import View

class Productview(CreateView):
	model = product
	fields ='__all__'
	
class Catergoryview(CreateView):
	model = catergory
	fields ='__all__'
	success_url = reverse_lazy('catergory')

class ProductUpdate(UpdateView):
	model = product
	fields = '__all__'
	template_name_suffix = '_update_form'

class productDelete(DeleteView):
	model = product
	success_url = reverse_lazy('productlist')

class productlist(ListView):
	model = product

class ProductDetailView(DetailView):
	queryset = product.objects.all()
	template_name = 'goodies/product_detail.html'

class homeview(View):
	def get(self, request):
		return render(request,'goodies/home.html')



