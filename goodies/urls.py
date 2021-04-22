from django.urls import path, include
from . import views
from goodies.views import(Productview, Catergoryview, ProductUpdate,
 productDelete, productlist, ProductDetailView, homeview)

urlpatterns = [
    # path('productform', Productview.as_view(), name='productform'),
    path('productform', views.Productview, name='productform'),
    # path ('Catergoryform', Catergoryview.as_view(), name = 'catergory'),
    path('Catergoryform', views.Catergoryview, name='catergory'),
    # path('updateproduct/<int:pk>/update',ProductUpdate.as_view(), name='updateproduct'),
    path('updateproduct/<int:id>/update',views.ProductUpdate, name='updateproduct'),
    path('deleteproduct/<int:pk>/delete', productDelete.as_view(), name='deleteproduct'),
    path('product-list', productlist.as_view(), name='productlist'),
    path('<int:pk>/', ProductDetailView.as_view(),  name='product-detail'),
    path('', homeview.as_view(),name=''),
    path('stockall', views.stockall, name='stockall'),
    path('lowstock', views.stocklow, name='lowstock'),
    path('highstock', views.highstock, name='highstock'),
    path('reports', views.reports, name='reports'),
    path('pdfview',views.render_pdf_view),
    path('remainstock', views.stockremaining, name='remainstock'),
]
