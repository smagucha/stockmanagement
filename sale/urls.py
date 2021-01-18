from django.urls import path
from . import views
from .views import saleview, SaleUpdate, saleDelete, salelist, saleDetailView

urlpatterns =[
	path('saleform', saleview.as_view()),
	path('updatesale/<int:pk>/update', SaleUpdate.as_view()),
	path('deletesale/<int:pk>/delete', saleDelete.as_view()),
    path('salelist', salelist.as_view(), name='salelist'),
    path('<int:pk>/', saleDetailView.as_view(),  name='sale-detail'),
]
