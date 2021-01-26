from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import product, catergory
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Sum
from sale.models import Sale
from .forms import DateForm
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

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
	context = {
	"title": title,
	"queryset": queryset,
	}
	return render(request, "goodies/stockall.html",context)

def stocklow(request):
	queryset=product.objects.values('name','productcatergory','weight').annotate(Sum('quantity'))
	context ={
	"queryset": queryset,
	}
	return render(request, 'goodies/lowstock.html',context)

def highstock(request):
	queryset=product.objects.values('name','productcatergory','weight').annotate(Sum('quantity'))
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


def reports(request):
	if request.method == 'POST':
		form = DateForm(request.POST)
		if form.is_valid():
			queryset = product.objects.filter(date_created__range=(form.cleaned_data['start_date'],
				form.cleaned_data['end_date']))
			print(queryset, '\n')
			form = DateForm()
			return HttpResponseRedirect('pdfview')
	else:
		form = DateForm()
	return render (request, 'goodies/reports.html', {'form': form})
"""
def stockreport(request):
	queryset = product.objects.filter(date_created__range=(date(2020,1,13), date(2021, 1, 16)))
	return render(request, 'goodies/stockreport.html',{'queryset': queryset})
"""
