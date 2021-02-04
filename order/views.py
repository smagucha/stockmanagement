from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from  django.views import View
from order.models import order

class home(View):
    def get(self, request):
        return render(request, 'order/home.html')




class Orderview(CreateView):
    model = order
    fields ='__all__'

class orderupdate(UpdateView):
    model = order
    fields ='__all__'

class orderdelete(DeleteView):
    model = order
    success_url = reverse_lazy('orderlist')

class orderlist(ListView):

    model = order


class orderdetail( DetailView):
	queryset = order.objects.all()
	template_name = 'order/order_detail.html'
