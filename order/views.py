from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from  django.views import View
from order.models import Order
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from goodies.models import Product


class home(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    def get(self, request):
        return render(request, 'order/home.html')

# class Orderview(PermissionRequiredMixin, CreateView):
#     permission_required = 'order.add_order'
#     model = order
#     fields ='__all__'
#     login_url = '/accounts/login'
@permission_required('order.add_order', login_url='/loginpage/')
def Orderview(request):
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            form=OrderForm()
            orderquantity= int(request.POST.get('quantity'))
            d=request.POST.get('product')
            good= Product.objects.get(id = d)
            good.quantity -= orderquantity 
            good.save()
            return redirect('orderlist')
    else:
        form=OrderForm()
        return render(request, 'order/order_form.html',{'form':form})

# class orderupdate(PermissionRequiredMixin, UpdateView):
#     model = order
#     fields ='__all__'
#     permission_required = 'order.change_order'
#     login_url = '/accounts/login'

@permission_required('order.change_order', login_url='/loginpage/')
def orderupdate(request, pk):
    obj = Order.objects.get(id = pk)
    productid = obj.product.id
    obj1= Product.objects.get(id = productid)
    form = OrderForm(request.POST or None, instance= obj)
    if form.is_valid():
        obj1.quantity += obj.quantity
        obj1.save()
        print('this is before update', obj1.quantity)
        form.save()
        orderquantity= int(request.POST.get('quantity'))
        obj1.quantity -= orderquantity
        obj1.save()
        print('this is after update', obj1.quantity)
        return redirect('orderlist')
    
   
    return render(request, 'order/order_update_form.html',{'form': form, 'obj':obj })

# class orderdelete(PermissionRequiredMixin, DeleteView):
#     model = Order
#     success_url = reverse_lazy('orderlist')
#     permission_required = 'order.delete_order'
#     login_url = '/accounts/login'

@permission_required('order.delete_order', login_url='/loginpage/')
def orderdelete(request, pk):
    obj = Order.objects.get(id=pk)
    productid=obj.product.id
    obj1 = Product.objects.get(id = productid)
    if request.method =='POST':
        obj1.quantity += obj.quantity
        obj1.save()
        obj.delete()
        return redirect('orderlist')
    return render(request, 'order/order_confirm_delete.html',{'obj': obj})


# class orderlist(PermissionRequiredMixin,ListView):
#     model = Order
#     permission_required = 'order.view_order'
#     login_url = '/accounts/login'

@login_required(login_url='/loginpage/')
def orderlist(request):
    obj = Order.objects.all()
    return render(request, 'order/order_list.html', {'obj': obj})



# class orderdetail(LoginRequiredMixin, DetailView):
# 	queryset = Order.objects.all()
# 	template_name = 'order/order_detail.html'
@login_required(login_url='/loginpage/')
def  orderdetail(request, pk):
    obj = Order.objects.get(id =pk)
    return render(request, 'order/order_detail.html', {'obj': obj})
   