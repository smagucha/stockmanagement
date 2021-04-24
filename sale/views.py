from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Sale
from django.urls import reverse_lazy
from .forms import saleform
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .forms import DateForm



# class saleview(PermissionRequiredMixin,CreateView):
# 	permission_required = 'sale.add_sale'
# 	model = Sale
# 	fields ='__all__'
# 	login_url = '/accounts/login'

@permission_required('sale.add_sale', login_url='/loginpage/')
def saleview(request):
	if request.method == 'POST':
		form= saleform(request.POST)
		if form.is_valid():
			your_object = form.save(commit=False)
			your_object.serverby = request.user
			your_object.save()
			form = saleform()
		return redirect('salelist')
	else:
		form = saleform()
		return render(request, 'sale/sale_form.html', {'form': form})




# class SaleUpdate(PermissionRequiredMixin,UpdateView):
# 	permission_required = 'sale.change_sale'
# 	model = Sale
# 	fields = '__all__'
# 	template_name_suffix = '_update_form'
# 	login_url= '/accounts/login'

@permission_required('sale.add_sale', login_url='/loginpage/')
def SaleUpdate(request, pk):
	obj = Sale.objects.get(id =pk)
	if request.method =='POST':
		form = saleform(request.POST or None, instance= obj)
		if form.is_valid():
			form.save()
			return redirect('salelist')
	else:
		form = saleform(request.POST or None, instance= obj)
		return render(request, 'sale/sale_update_form.html', {'form':form, 'obj':obj})


# class saleDelete(PermissionRequiredMixin, DeleteView):
# 	permission_required = 'sale.delete_sale'
# 	model = Sale
# 	success_url = reverse_lazy('productlist')
# 	login_url='/accounts/login'

@permission_required('sale.delete_sale', login_url='/loginpage/')
def saleDelete(request, pk):
	obj = Sale.objects.get(id =pk)
	if request.method =='POST':
		obj.delete()
		return redirect('salelist')
	else:
		return render(request, 'sale/sale_confirm_delete.html', {'obj':obj})


# class salelist(PermissionRequiredMixin,ListView):
# 	permission_required='sale.view_sale'
# 	model = Sale
# 	login_url='/accounts/login'
@permission_required('sale.view_sale', login_url='/loginpage/')
def salelist(request):
	obj = Sale.objects.all()
	return render(request, 'sale/sale_list.html', {'obj':obj})




# class saleDetailView(LoginRequiredMixin, DetailView):
# 	queryset = Sale.objects.all()
# 	template_name = 'sale/sale_detail.html'
# 	login_url='/accounts/login'

def saleDetailView(request, pk):
	obj = Sale.objects.get(id =pk)
	return render(request, 'sale/sale_detail.html', {'obj':obj})


