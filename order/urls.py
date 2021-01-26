from django.urls import path
from . import views
from order.views import Orderview
urlpatterns = [
    path('Orderview',Orderview.as_view()),

]
