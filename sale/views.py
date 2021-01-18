from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Sale

class saleview(CreateView):
	model = Sale
	fields ='__all__'
	
class ProductUpdate(UpdateView):
	model = Sale
	fields = '__all__'
	template_name_suffix = '_update_form'
	

