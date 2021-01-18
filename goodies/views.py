from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import product, catergory
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Sum

class Productview(PermissionRequiredMixin,CreateView):
	permission_required = 'goodies.add_product'
	model = product
	fields ='__all__'
	login_url = '/accounts/login'
	
	
class Catergoryview(PermissionRequiredMixin,CreateView):
	permission_required = 'goodies.add_catergory'
	model = catergory
	fields ='__all__'
	success_url = reverse_lazy('catergory')
	login_url = '/accounts/login'
	

class ProductUpdate(PermissionRequiredMixin, UpdateView):
	permission_required = 'goodies.change_product'
	model = product
	fields = '__all__'
	template_name_suffix = '_update_form'
	login_url = '/accounts/login'
	

class productDelete(PermissionRequiredMixin, DeleteView):
	permission_required = 'goodies.delete_product'
	model = product
	success_url = reverse_lazy('productlist')
	login_url = '/accounts/login'
	

class productlist(LoginRequiredMixin, ListView):
	#permission_required = 'goodies.view_product'
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
	title = 'ALL sale'
	queryset=product.objects.values('name','productcatergory','weight').annotate(Sum('quantity'))
	print (queryset)
	context = {
	"title": title,
	"queryset": queryset,
	}
	return render(request, "goodies/stockall.html",context)

	
	




