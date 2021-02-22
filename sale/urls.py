from django.urls import path
from . import views
from .views import saleview, SaleUpdate, saleDelete, salelist, saleDetailView

urlpatterns =[
	path('saleform', saleview.as_view(), name='saleform'),
	path('updatesale/<int:pk>/update', SaleUpdate.as_view() , name ='updatesale'),
	path('deletesale/<int:pk>/delete', saleDelete.as_view(), name='deletesale'),
    path('salelist', salelist.as_view(), name='salelist'),
    path('sale/<int:pk>/', saleDetailView.as_view(),  name='sale-detail'),
    path('allsale', views.allsale, name='allsale'),
	path('salereport', views.salereport, name= 'salereport'),
]
