from django.urls import path
from . import views
from .views import Orderview

urlspattern = [
    path('Orderview',Orderview.as_view(),)
]
