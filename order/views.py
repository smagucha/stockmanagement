from django.shortcuts import render
from django.views.generic.edit import CreateView

from order.models import order

class Orderview(CreateView):
    model = order
    fields ='__all__'

class orderupdate(UpdateView):
    model = order
    fields ='__all__'

class orderdelete(DeleteView):
    model = order
    success_url = reverse_lazy('oredrlist')

class orderlist(ListView):
    model = order
