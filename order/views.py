from django.shortcuts import render
from django.views.generic import Createview
from .models import order

class Orderview(Createview):
    model = Order
    fields ='__all__'
