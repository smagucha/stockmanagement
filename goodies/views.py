from django.shortcuts import render,redirect
#from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormMixin
#from django.views.generic.detail import DetailView
#from django.views.generic.list import ListView
from .models import product, catergory
#from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
#from django.db.models import Sum
from .forms import DateForm, productform, catergoryform, AddProduct
#from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from datetime import datetime
from django.http import HttpResponse
#from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# class Productview(PermissionRequiredMixin,CreateView):
# 	permission_required = 'goodies.add_product'
# 	model = product
# 	fields ='__all__'
# 	login_url = '/accounts/login'

@permission_required('goodies.add_product', login_url='/loginpage/')
def Productview(request):
	if request.method=='POST':
		form = productform(request.POST)
		if form.is_valid():
			form.save()
			form = productform()
			return redirect('productlist')
	else:
		form = productform()
		return render(request, 'goodies/product_form.html',{'form':form})


# class Catergoryview(PermissionRequiredMixin,CreateView):
# 	permission_required = 'goodies.add_catergory'
# 	model = catergory
# 	fields ='__all__'
# 	success_url = reverse_lazy('catergory')
# 	login_url = '/accounts/login'

@permission_required('goodies.add_catergory', login_url='/loginpage/')
def Catergoryview(request):
	if request.method =='POST':
		form = catergoryform(request.POST)
		if form.is_valid():
			form.save()
			form = catergoryform()
			return redirect('productlist')
	else:
		form = catergoryform()
		return render(request, 'goodies/catergory_form.html', {'form': form})


# class ProductUpdate(PermissionRequiredMixin, UpdateView):
# 	permission_required = 'goodies.change_product'
# 	model = product
# 	fields = '__all__'
# 	template_name_suffix = '_update_form'
# 	login_url = '/accounts/login'

@permission_required('goodies.change_product', login_url='/loginpage/')
def ProductUpdate(request,id):
	obj = product.objects.get(id=id)
	#if request.method(request.POST or None, instance=obj):
	form = productform(request.POST or None, instance= obj)
	if form.is_valid():
		form.save()
		return redirect('productlist')
	return render(request, 'goodies/product_update_form.html', {'obj':obj,'form':form})



# class productDelete(PermissionRequiredMixin, DeleteView):
# 	permission_required = 'goodies.delete_product'
# 	model = product
# 	success_url = reverse_lazy('productlist')
# 	login_url = '/accounts/login'

@permission_required('goodies.delete_product', login_url='/loginpage/')
def  productDelete(request, pk):
	obj= product.objects.get(pk=pk)
	if request.method =='POST':
		obj.delete()
		return redirect('productlist')
	return render(request, 'goodies/product_confirm_delete.html', {'obj':obj})


# class productlist(LoginRequiredMixin,FormMixin, ListView):
# 	model = product
# 	login_url = '/accounts/login'
# 	redirect_field_name = ''
# 	form_class = DateForm

@login_required(login_url='/loginpage/')
def productlist(request):
	if request.method == 'POST':
		form = DateForm(request.POST)
		if form.is_valid():
			queryset = product.objects.filter(date_created__range=(form.cleaned_data['start_date'],
				form.cleaned_data['end_date']))
			print(queryset, '\n')
		form = DateForm()
		return render (request, 'goodies/product_list.html', {'form': form, 'queryset': queryset})
	else:
		queryset = product.objects.all()
		form = DateForm()
		return render(request, 'goodies/product_list.html',{'form': form,'queryset':queryset})
	# queryset = product.objects.all()
	# return render(request, 'goodies/product_list.html',{'queryset':queryset})


# class ProductDetailView(LoginRequiredMixin, DetailView):
# 	queryset = product.objects.all()
# 	template_name = 'goodies/product_detail.html'
# 	login_url = '/accounts/login'
@login_required(login_url='/loginpage/')
def ProductDetailView(request, pk):
	obj= product.objects.get(pk=pk)
	return render(request, 'goodies/product_detail.html', {'obj':obj})

@login_required(login_url='/loginpage/')
def addproduct(request,id):
	obj = product.objects.get(id=id)
	if request.method =='POST':
		form = AddProduct(request.POST)
		if form.is_valid():
			add=int(request.POST.get('add_quantity'))
			obj.quantity +=add 
			obj.save()
			return redirect('productlist')	
	else:
		form = AddProduct()
		return render(request, 'goodies/addproduct.html', {'form':form})

class homeview(LoginRequiredMixin, View):
	def get(self, request):
		return render(request,'goodies/home.html')
	login_url = '/accounts/login'

def stocklow(request):
	queryset=product.objects.all()
	context ={
	"queryset": queryset,
	}
	return render(request, 'goodies/lowstock.html',context)

def highstock(request):
	queryset=product.objects.all()
	context ={
	"queryset": queryset,
	}
	return render(request, 'goodies/toomuchstock.html',context)


def render_pdf_view(request):
    template_path = 'goodies/stockreport.html'
    queryset = product.objects.all()
    context = {'queryset': queryset}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #in order to download add attachment
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# def reports(request):
# 	if request.method == 'POST':
# 		form = DateForm(request.POST)
# 		if form.is_valid():
# 			queryset = product.objects.filter(date_created__range=(form.cleaned_data['start_date'],
# 				form.cleaned_data['end_date']))
# 			print(queryset, '\n')
# 		form = DateForm()
# 		return render (request, 'goodies/reports.html', {'form': form, 'queryset': queryset})
# 	else:
# 		queryset = product.objects.all()
# 		form = DateForm()
# 		return render (request, 'goodies/reports.html', {'form': form, 'queryset': queryset})


