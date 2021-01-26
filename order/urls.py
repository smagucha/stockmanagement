from django.urls import path
from . import views
from order.views import Orderview
urlpatterns = [
    path('Orderview',Orderview.as_view()),
    path('updateorder/<int:pk>/update',ProductUpdate.as_view(),
    path('deleteorder/<int:pk>/delete', productDelete.as_view()),
    path('orderlist', productlist.as_view(), name='productlist')

]
