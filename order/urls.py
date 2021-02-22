from django.urls import path
from . import views
from order.views import Orderview, orderupdate, orderdelete, orderlist,orderdetail, home
urlpatterns = [
    path('Orderview',Orderview.as_view(), name='orderview'),
    path('order/<int:pk>/update',orderupdate.as_view(), name='updateorder'),
    path('order/<int:pk>/delete', orderdelete.as_view(),name='deleteorder'),
    path('orderlist', orderlist.as_view(), name= 'orderlist'),
    path('order/<int:pk>/', orderdetail.as_view(),  name='order-detail'),
    ]
