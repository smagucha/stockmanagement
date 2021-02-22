from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from  django.views import View
from order.models import order
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required


class home(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    def get(self, request):
        return render(request, 'order/home.html')

class Orderview(PermissionRequiredMixin, CreateView):
    permission_required = 'order.add_order'
    model = order
    fields ='__all__'
    login_url = '/accounts/login'

class orderupdate(PermissionRequiredMixin, UpdateView):
    model = order
    fields ='__all__'
    permission_required = 'order.change_order'
    login_url = '/accounts/login'

class orderdelete(PermissionRequiredMixin, DeleteView):
    model = order
    success_url = reverse_lazy('orderlist')
    permission_required = 'order.delete_order'
    login_url = '/accounts/login'

class orderlist(PermissionRequiredMixin,ListView):
    model = order
    permission_required = 'order.view_order'
    login_url = '/accounts/login'


class orderdetail(LoginRequiredMixin, DetailView):
	queryset = order.objects.all()
	template_name = 'order/order_detail.html'
   