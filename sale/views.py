from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Sale
from django.urls import reverse_lazy
from .forms import saleform

class saleview(CreateView):
	model = Sale
	fields ='__all__'


	
class SaleUpdate(UpdateView):
	model = Sale
	fields = '__all__'
	template_name_suffix = '_update_form'

class saleDelete(DeleteView):
	model = Sale
	success_url = reverse_lazy('productlist')
	


class salelist(ListView):
	model = Sale
	

class saleDetailView(DetailView):
	queryset = Sale.objects.all()
	template_name = 'sale/sale_detail.html'

