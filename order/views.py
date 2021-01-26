from django.shortcuts import render
from django.views.generic.edit import CreateView

from order.models import order

class Orderview(CreateView):
    model = order
    fields ='__all__'
