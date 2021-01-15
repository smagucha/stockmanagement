from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import product, catergory
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class Productview(LoginRequiredMixin,CreateView):
	model = product
	fields ='__all__'
	login_url = '/accounts/login'
	
	
class Catergoryview(LoginRequiredMixin,CreateView):
	model = catergory
	fields ='__all__'
	success_url = reverse_lazy('catergory')
	login_url = '/accounts/login'
	

class ProductUpdate(LoginRequiredMixin, UpdateView):
	model = product
	fields = '__all__'
	template_name_suffix = '_update_form'
	login_url = '/accounts/login'
	

class productDelete(LoginRequiredMixin, DeleteView):
	model = product
	success_url = reverse_lazy('productlist')
	login_url = '/accounts/login'
	

class productlist(LoginRequiredMixin, ListView):
	model = product
	login_url = '/accounts/login'
	redirect_field_name = ''

class ProductDetailView(LoginRequiredMixin, DetailView):
	queryset = product.objects.all()
	template_name = 'goodies/product_detail.html'
	login_url = '/accounts/login'
	

class homeview(LoginRequiredMixin, View):
	def get(self, request):
		return render(request,'goodies/home.html')
	login_url = '/accounts/login'
	

def stockall(request):
	stock = product.objects.all()
	y = []
	for objects in stock:
		if objects.name == objects.name and objects.productcatergory==objects.productcatergory and objects.weight==objects.weight:
			#quantity = objects.quantity + objects.quantity
			y.append(objects.quantity)	
		else:
			pass
	print(sum(y))

	return render(request, 'goodies/stockall.html')




