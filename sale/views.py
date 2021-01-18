from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Sale
from django.urls import reverse_lazy
from .forms import saleform
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


	
class saleview(PermissionRequiredMixin,CreateView):
	permission_required = 'sale.add_sale'
	model = Sale
	fields ='__all__'
	login_url = '/accounts/login'


	
class SaleUpdate(PermissionRequiredMixin,UpdateView):
	permission_required = 'sale.change_sale'
	model = Sale
	fields = '__all__'
	template_name_suffix = '_update_form'
	login_url= '/accounts/login'

class saleDelete(PermissionRequiredMixin, DeleteView):
	permission_required = 'sale.delete_sale'
	model = Sale
	success_url = reverse_lazy('productlist')
	login_url='/accounts/login'
	


class salelist(LoginRequiredMixin,ListView):
	model = Sale
	login_url='/accounts/login'
	

class saleDetailView(LoginRequiredMixin, DetailView):
	queryset = Sale.objects.all()
	template_name = 'sale/sale_detail.html'
	login_url='/accounts/login'

