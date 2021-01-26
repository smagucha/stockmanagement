from django.urls import path, include
from . import views
from goodies.views import(Productview, Catergoryview, ProductUpdate,
 productDelete, productlist, ProductDetailView, homeview)

urlpatterns = [
    path('productform', Productview.as_view()),
    path ('Catergoryform', Catergoryview.as_view(), name = 'catergory'),
    path('updateproduct/<int:pk>/update',ProductUpdate.as_view()),
    path('deleteproduct/<int:pk>/delete', productDelete.as_view()),
    path('product-list', productlist.as_view(), name='productlist'),
    path('<int:pk>/', ProductDetailView.as_view(),  name='product-detail'),
    path('', homeview.as_view(),),
    path('stockall', views.stockall),
    path('lowstock', views.stocklow),
    path('highstock', views.highstock),
    path('reports', views.reports),
    path('pdfview',views.render_pdf_view),
    #path('stockreport', views.stockreport)

]
