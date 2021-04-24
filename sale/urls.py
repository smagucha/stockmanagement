from django.urls import path
from . import views
#from .views import saleview, SaleUpdate, saleDelete, salelist, saleDetailView

urlpatterns =[
	# path('saleform', saleview.as_view(), name='saleform'),
	path('saleform', views.saleview, name='saleform'),
	# path('updatesale/<int:pk>/update', SaleUpdate.as_view() , name ='updatesale'),
	path('updatesale/<int:pk>/update', views.SaleUpdate , name ='updatesale'),
	# path('deletesale/<int:pk>/delete', saleDelete.as_view(), name='deletesale'),
	path('deletesale/<int:pk>/delete', views.saleDelete, name='deletesale'),
    # path('salelist', salelist.as_view(), name='salelist'),
    path('salelist', views.salelist, name='salelist'),
    #path('sale/<int:pk>/', saleDetailView.as_view(),  name='sale-detail'),
    path('sale/<int:pk>/', views.saleDetailView,  name='sale-detail'),
]
